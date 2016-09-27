# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:47:35 2016

@author: MagicWang
"""
import threading
import time
import datetime
import socket

a=3

def test():
    global a
    a=1
    print 'a=%d'%a

def main_thread():
    global a
    time.sleep(1)
    print a

def change(lista):
    lista.remove('a')

if __name__=="__main__":
#    thread1=threading.Thread(target=test,args=())
#    thread2=threading.Thread(target=main_thread,args=())
#    thread2.start()
#    thread1.start()
#    while 1:
#        pass
#    with open('ss.jpg','wb') as fw:
#        fw.write('')


#    for i in range(100):
#        print datetime.datetime.now()
#        time.sleep(0.00001)


#    host='127.0.0.1'
#    port=7000
#    RECV_BUFFER=4096
#
#    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#    client_socket.settimeout(2)
#    client_socket.connect((host,port))
#    
#    c_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#    c_socket.settimeout(2)
#    c_socket.connect((host,port))
#    
#    client_socket.close()

    a=['a','b','c']
    change(a)
    print a
    