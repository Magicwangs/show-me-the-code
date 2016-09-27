# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:28:18 2016

@author: MagicWang
"""
import socket
import select
import sys
import traceback
import threading
import struct
import hashlib
import time
import datetime

#broadcast chat messages
def broadcast_data(sock,message,server_socket,CONNECTION_LIST):
    for s in CONNECTION_LIST:
        #排除服务器和本机
        if s!=server_socket and s!=sock:
            try:
                s.send(message)
            except:
                #print except error
                traceback.print_exc()
                s.close()
                CONNECTION_LIST.remove(s)

def MD5Check(filename,md5hex):
    with open(filename,'rb') as fr:
        md5_cal=hashlib.md5()
        #处理大文件，内存不够时
        while 1:
            data=fr.read(10240)
            if not data:
                break
            md5_cal.update(data)
        if md5_cal.hexdigest()==md5hex:
            print "MD5 Check OK"
        else:
            print "MD5 Check ERROR"


#close client
def close_client_socket(sock,server_socket,CONNECTION_LIST):
    #getpeername():获取socket的host和port
    clienthost,clientport=sock.getpeername()
    broadcast_data(sock,'[{}:{}]已经下线\n'.format(clienthost,clientport),server_socket,CONNECTION_LIST)
    #控制台输出    
    print '客户端[{}:{}]已经下线了\n'.format(clienthost,clientport)
    #控制台刷新
    sys.stdout.flush()
    sock.close()
    CONNECTION_LIST.remove(s)

def check_data(sock,server_socket,msg,CONNECTION_LIST,RECV_BUFFER):
    check_id=msg[:6]
    data=msg[6:]
    if check_id=='<text>':
        try:
            if data:
                clienthost, clientport = sock.getpeername()
                thismsg='<{}:{}>说:{}'.format(clienthost, clientport, data)
                threading.Thread(target=broadcast_data,args=(sock,thismsg,server_socket,CONNECTION_LIST)).start()
        except:
            traceback.print_exc()
            close_client_socket(sock,server_socket,CONNECTION_LIST)
        data=''
        return data,0
    else:
        global recv_size
        recv_size+=RECV_BUFFER
        return msg[:],1

def write_data(file_name,file_size,RECV_BUFFER,sock,md5_recv,server_socket,CONNECTION_LIST):
    global file_sock,first_flag,recv_size
    recv_size=0
    packet_Num=0
    print datetime.datetime.now()
    with open(file_name,'wb') as fw:
        while(recv_size<file_size):
            if((file_size-recv_size)<RECV_BUFFER):
                file_data=sock.recv(file_size-recv_size)
                print file_size-recv_size
                sys.stdout.flush()
#                file_data,write_flag=check_data(sock,server_socket,file_data,CONNECTION_LIST,RECV_BUFFER)
                recv_size=file_size
                packet_Num+=1
                print 'packet_Num is',packet_Num
            else:
                packet_Num+=1
                file_data=sock.recv(RECV_BUFFER)
                recv_size+=RECV_BUFFER
#                file_data,write_flag=check_data(sock,server_socket,file_data,CONNECTION_LIST,RECV_BUFFER)
                time.sleep(0.001)
#            if write_flag:
            fw.write(file_data)
    print datetime.datetime.now()
    rlist=[sock,]
    r_socket,w_sockets,e_sockets=select.select(rlist,[],[])
    for s in r_socket:
        data=s.recv(RECV_BUFFER)
#    print 'OVER'
#    print data[:10]
    sys.stdout.flush()
    if data=='<file>over':
        print "file transfrom over"
#        file_sock=None
        first_flag=1
        recv_size=0
        MD5Check(file_name,md5_recv)
        file_sock.close()
        
    
if __name__=="__main__":
    ###全局变量###    
    global file_sock,first_flag,recv_size
    file_sock=socket.socket()
    first_flag=1
    recv_size=0
    ###
    ADDRESS=('127.0.0.1',7000)
    RECV_BUFFER=4096
    CONNECTION_LIST=[]
    try:
        #AF_UNIX用于同一台机器上的进程间通信，AF_INET对于IPV4协议的TCP和UDP
        #SOCK_STREAM:面向连接TCP；SOCK_DGRAM无连接UDP
        server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #socket option:当socket关闭后，本地端用于该socket的端口号立刻就可以被重用
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(ADDRESS)
        #最大连接数为10
        server_socket.listen(10)
    except:
        print 'Socket Create ERROR!'
        sys.exit()
    #add server_socket
    CONNECTION_LIST.append(server_socket)    
    
    HEAD_STRUCT='128sIq32s' 
    info_struct = struct.calcsize(HEAD_STRUCT)
    
    #多客户端聊天，不能采用堵塞的accept(),可以通过select轮询
    while 1:
        #r_sockets中有两种情况：
        #一是服务端socket可读，表示有新的客户端连接到聊天室
        #二是客户端socket可读，表示聊天室里有某个客户端在发言
        r_sockets,w_sockets,e_sockets=select.select(CONNECTION_LIST,[],[])
        for s in r_sockets:
            #如果聊天列表中的服务器端socket可读，则把socket接受得到的客户端socket添加到连接列表中。
            if s==server_socket:
                clientsock,clientaddr=s.accept()
                CONNECTION_LIST.append(clientsock)
                try:
                    broadcast_data(clientsock,'[{}:{}]进入房间\n'.format(*clientsock.getpeername()),server_socket,CONNECTION_LIST)
                    print '当前聊天室人数：{}\n'.format(len(CONNECTION_LIST)-1)
#                    sys.stdout.flush()
                except:
                    traceback.print_exc()
            elif s==file_sock:
                if first_flag:
                    file_info=s.recv(info_struct)
                    file_name2,filename_size,file_size,md5_recv=struct.unpack(HEAD_STRUCT, file_info)
                    file_name=file_name2[:filename_size]
                    file_name='recv'+'\\'+file_name
                    first_flag=0
                    CONNECTION_LIST.remove(file_sock)
                    print "file transfrom start"
                    threading.Thread(target=write_data,args=(file_name,file_size,RECV_BUFFER,s,md5_recv,server_socket,CONNECTION_LIST)).start()
                    
            #如果聊天列表中的客户端socket可读，则把socket中的数据取出（即发言记录）分发给连接列表中的其它客户端socket
            else:
                try:
                    data=s.recv(RECV_BUFFER)
                    if data:
                        #如果客户端输入<exit>就退出
                        if data=='<exit>':
                            close_client_socket(s,server_socket,CONNECTION_LIST)
                        elif data=='<file>start':
                            file_sock=s
                        else:
                            clienthost, clientport = s.getpeername()
                            msg='<{}:{}>说:{}'.format(clienthost, clientport, data)
                            broadcast_data(s,msg,server_socket,CONNECTION_LIST)
                except:
                    traceback.print_exc()
                    close_client_socket(s,server_socket,CONNECTION_LIST)
                    continue
    server_socket.close()
                    