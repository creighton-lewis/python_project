#Install necessary libraries 
import requests 
import os 
from subdomains import sub_end
def tech():
    if 'sub_end' == None:
        input=("Write target or file with subdomains:")
    try: 
            os.system(f"nmap -sV -sU --top-ports 50 -oN {input}_tech")
    except: 
         ("Target not found, using file")
    os.system(f"nmap -sV -sU --top-ports 50 -oN {input}_tech -D RND:5 -iL {input}")   
    if 'sub_end' in globals():
        print('sub_end')
    print ("Running tech scan for {sub_end}")
    os.system(f"nmap -sV -sU --top-ports 50 -oN {sub_end}_tech -D RND:5 -iL {sub_end}")   
tech()
