# -*- coding: utf-8 -*-
# python2.7
"""
Created on Fri Oct 28 19:19:58 2016

@author: MagicWang
"""
import os
from hashlib import  sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8)##随机生成8个字节的字符串,用作随机加密的Key
    
    assert 8 == len(salt)  ##断言，如果不为真就出现异常
    assert isinstance(salt, str)
    
    if isinstance(password, unicode):
        password = password.encode('UTF-8')
    
    assert isinstance(password, str)
    
    result = password
    for i in xrange(10):
        ##选择 SHA-256 算法使用 HMAC 对密码和 salt 进行 10 次叠代混淆
        result = HMAC(result, salt, sha256).digest()
    
    return salt+result

def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])

if __name__=="__main__":
    password = raw_input("请设置你的密码：")
    hashed = encrypt_password(password)
    inputPassword = raw_input("请输入你的密码：")
    print "Yes,you got it" if validate_password(hashed, inputPassword) else "It's Wrong"