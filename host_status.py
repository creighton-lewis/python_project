import requests 
import os 
import nmap
import sys 
import subprocess
#import libnmap
nm=nmap 

file = input ("Select file:")
s = file.readline()
print(s)
for s in file:
  nm.scan(hosts='s', arguments='-n -sP')

