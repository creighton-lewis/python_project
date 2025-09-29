
import os 
#import nmap
#Defining variables 

print("Welcome to ReconTool")
global target
target = input("Enter company name: ")
print (target)
end = target.rsplit(".", 1)[-1]

def subdomain_enum():
    print("Subdomain Enumeration Selected") 
    os.system(f"sudo nmap --script smtp-enum-users -Pn --top-ports 1 -sn {target} -oN {target}_dnsbrute")
    
subdomain_enum();