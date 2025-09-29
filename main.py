#Import relevant libraries
import os 
import socket 
import requests 

target = input("Enter company name: ")
print (target)
end = target.rsplit(".", 1)[-1]
print ("Welcome to the Reconnaissance Tool. For subdomain enumeration, press one")
#try:
#    site_ip = socket.gethostbyname(target)
 #   print(site_ip, end ='')
#except socket.gaierror:
#    print ("Invalid site")

def option_1():
    print("Subdomain Enumeration Selected")
    os.system(f"subfinder -d {target} -o {target}_subdomains")
    os.system(f"assetfinder {target} >> {target}_subdomains")
    os.system(f"gobuster dns -d {target} -w ~/lst/sub_list -o {target}_gobuster -t 70 --wildcard")
    os.system(f"sed -i 's/www.//g' {target}_gobuster")
    os.system(f"sed -i 's/Found://g' {target}_gobuster")
    os.system(f"sort -u {target}_subdomains.txt -o {target}_subdomains")
    print(f"Subdomain enumeration completed. Results saved in {target}_subdomains")

    os.system(f"grep ptr")


def option_2():
    print("Tech Enumeration")
    os.system(f"sudo nmap --top-ports 30 -iL {target} -oN {target}_topportscan.txt -D RND:10 --data-length 20 --script vuln,auth")
    print(f"Port scanning completed. Results saved in {target}_fullportscan.txt and {target}_topportscan.txt")