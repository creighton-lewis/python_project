#
import requests 
import os 
import subprocess 
from main import target
def subdomain_enum():
    print("Subdomain Enumeration Selected")
os.system(f"nmap -sV --script dns-brute -sn -n {target} -oN {target}_dnsbrute")
os.system(f"rm {target}_dnsbrute")

subdomain_enum()
os.system(f"subfinder -d {target} -o {target}_subdomains")
os.system(f"amass enum -d {target} -o {target}_amass")
os.system(f"assetfinder --subs-only {target} >> {target}_subdomains")
def gobuster_sub():
    os.system(f"gobuster dns -d {target} -w ~/lst/sub_list -o {target}_gobuster -t 70 --wildcard")
    os.system(f"sed -i 's/www.//g; s/Found://g' {target}_gobuster")
    os.system(f"cat {target}_clean")
    os.system(f"mv -f {target}_clean {target}_file")
    os.system(f"sort -u {target}_subdomains -o {target}_subdomains")
    os.system(f"{target}_gobuster >> {target}_subdomains")
    os.system(f"sort -u {target}_subdomains -o {target}_subdomains")
subdomain_enum()
gobuster_sub()
print(f"Subdomain enumeration completed. Results saved in {target}_subdomains")
#subdomain_enum();
#gobuster_sub();