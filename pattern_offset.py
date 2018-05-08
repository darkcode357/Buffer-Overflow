#!/usr/bin/python
#-*-coding: utf-8-*-
import subprocess
def pattern_offser(n1):
    subprocess.call(['/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb','-q'+n1])
