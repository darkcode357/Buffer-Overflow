#!/usr/bin/python
#-*-coding: utf-8-*-
import subprocess

n1 = raw_input("Digite o valor do EIP: ")
subprocess.call(['/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb','-q'+n1])
