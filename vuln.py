import os 
import requests
import argparse
from tech import target
from main import target 
if 'target' in globals:
    print ("Running vulnerability scan")
def vuln_scan():
    os.system(f"tmux split-screen")
    try:
        os.system(f"sudo nmap sV --script=vulners,auth -f --data-length 10 -D RND:6 {target}")
    except: 
        print ("Target not found, trying file")
        os.system(f"sudo nmap sV --script=vulners,auth -f --data-length 10 -D RND:6 -iL {target}")
def vuln_cleanup():
    os.system(f"sed -i 's/find//g' {target}")
def vuln_search():
    keyword=("Enter value to search for ")
    version=("Enter version name")

