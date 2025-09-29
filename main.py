#Import relevant libraries
import os 
import socket 
import requests 
from rich.console import console
#Install necessary programs 


def target():
    global target
    target = input("Enter company name: ")
    print (target)
    end = target.rsplit(".", 1)[-1]
  #  print ("Welcome to the Reconnaissance Tool. For subdomain enumeration, press one")
#try:
    #    site_ip = socket.gethostbyname(target)
 #   print(site_ip, end ='')
    #except socket.gaierror:
    #    print ("Invalid site")

def subdomain_enum():
    print("Subdomain Enumeration Selected")
    try:
        os.system(f"nmap --script dns-brute-enum -sn -n -iL {target} -oN {target}_dnsbrute")
    except: 
        print("Error with nmap dns-brute-enum")
    os.system(f"subfinder -d {target} -o {target}_subdomains")
    os.system(f"amass enum -d {target} -o {target}_amass")
    os.system(f"assetfinder --subs-only {target} >> {target}_subdomains")
    def gobuster_sub():
        os.system(f"gobuster dns -d {target} -w ~/lst/sub_list -o {target}_gobuster -t 70 --wildcard")
        os.system(f"sed -i 's/www.//g' {target}_gobuster")
        os.system(f"sed -i 's/Found://g' {target}_gobuster")
        os.system(f"tail -n +11 "target" >> "{target}_clean")
        os.system(f"cat "{target}_clean"))
            mv -f "{file}_clean" "$file"
exit
        os.system(f"sort -u {target}_subdomains.txt -o {target}_subdomains")
    print(f"Subdomain enumeration completed. Results saved in {target}_subdomains")

    os.system(f"grep ptr")
    os.system(f"")


def option_2():
    print("Tech Enumeration")
     try: 
        file = input("Enter file path")

    os.system(f"sudo nmap sV --top-ports 30 -iL {target} -oN {target}_topportscan.txt -D RND:10 --data-length 20 --script auth")
    print(f"Port scanning completed. Results saved in {target}_fullportscan.txt & {target}_topportscan.txt")