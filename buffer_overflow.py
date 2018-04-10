#!/usr/bin/python
#-*-coding: utf-8-*-
import sys
import subprocess

print'''\033[36m


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

\033[1m'''

print"[1] INSTALAR NMAP"
print"[2] SCANEAR IP DO ALVO"
print"[3] FAZER FUZZING NO ALVO"
print"[4] VALIDAR CRASH"
print"[5] GERAR PADRAO EIP"
print"[6] ENVIAR PADRAO EIP PRO ALVO PARA ENCONTRAR O ENDEREÇO EIP"
print"[7] VERIFICAR COM QUANTOS BYTES O EIP É ATINGIDO    "
print"[8] TESTAR CONTROLE SOBRE O EIP"
print"[9] VERIFICAR ESPAÇO PARA SHELLCODE"
print"[10] VERIFICAR CARACTERES HEXADECIMAL INVÁLIDOS"
print"[11] TESTAR EXECUÇÃO DE ENDEREÇO DE RETORNO"
print"[12] CRIAR SHELLCODE "

opcao = int(input("➤➤ ESCOLHA UMA OPÇÃO: "))
if opcao == 1:
	opcao = subprocess.call(["apt-get","install","nmap"])
	print(opcao)
	print"Execução finalizada"


if opcao == 2:
	ip = raw_input("➤➤ Digite o IP do alvo: ")
	opcao = subprocess.call(["nmap","-v","-sV","-Pn",ip])
	print(opcao)


if opcao == 3:
	opcao = subprocess.call(["python","fuzzing.py"])
	print(opcao)

if opcao == 4:
	opcao = subprocess.call(["python","crash.py"])
	print(opcao)


if opcao == 5:

        buffer = raw_input("➤➤ Digite a quantidade de bytes do fuzzing : ")
	opcao = subprocess.call(["python","pattern.py","create",buffer])
	print(opcao)
	print("➤➤ Copie toda a string padrão que foi gerada, da ultima letra até a primeira.")



if opcao == 6:
	opcao = subprocess.call(["python","eip.py"])
	print(opcao)



if opcao == 7:
	opcao = subprocess.call(["python","pattern_offset.py"])
	print(opcao)


if opcao == 8:
	opcao = subprocess.call(["python","subeip.py"])
	print(opcao)



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

