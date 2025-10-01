
import os 
import requests 
from urlextract import URLExtract
extractor = URLExtract
urls = extractor.find_urls(
print(urls) # prints: ['janlipovsky.cz']


#import nmap
#Defining variables 

print("Welcome to ReconTool")
global target
target = input("Enter company name: ")
print (target)
end = target.rsplit(".", 1)[-1]

def subdomain_enum():
    print("Subdomain Enumeration Selected") 
    os.system(f"sudo nmap --script dns-brute --top-ports 10 -D RND:7 -oN {target}_dnsbrute")
    os.system(f"cat {target}_dnsbrute")
    sub_end= '{target}_dnsbrute'
subdomain_enum()

def tech_enum():
    print ("Scanning for active tech")

    
tech_enum()
#dns burte only provides urls and ip addresses for common things; other scrips are not cinluded 