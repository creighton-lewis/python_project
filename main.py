#Import relevant libraries
import os 
import socket 
import requests 
import random
from TerminalMenu import simple_term_menu
#from rich.console import console
#Install necessary programs 

print("Welcome to ReconTool")
print("""\
           .                          _                          ..                                    
  .x88888x.                     u                     x .d88"                                     
 :8**888888╳.  :>              88Nu.   u.              5888R      x.    .        ..    .     :    
 f    `888888x.╱        u     '88888.o888c      .u     '888R    .@88k  z88u    .888: x888  x888.  
'       `*88888~     us888u.   ^8888  8888   ud8888.    888R   ~"8888 ^8888   ~`8888~'888╳`?888f` 
 ╲.    .  `?)╳.   .@88 "8888"   8888  8888 :888'8888.   888R     8888  888R     ╳888  888╳ '888>  
  `~=─^   ╳88> ~  9888  9888    8888  8888 d888 '88%"   888R     8888  888R     ╳888  888╳ '888>  
         ╳8888  ~ 9888  9888    8888  8888 8888.┼"      888R     8888  888R     ╳888  888╳ '888>  
         488888   9888  9888   .8888b.888P 8888L        888R     8888 ,888B .   ╳888  888╳ '888>  
 .xx.     88888╳  9888  9888    ^Y8888*""  '8888c. .┼  .888B .  "8888Y 8888"   "*88%""*88" '888!` 
'*8888.   '88888> "888*""888"     `Y"       "88888%    ^*888%    `Y"   'YP       `~    "    `"`   
  88888    '8888>  ^Y"   ^Y'                  "YP'       "%                                       
  `8888>    `888                                                                                  
   "8888     8%                                                                                   
    `"888x:─"                                                                                     / \_______/|__/      |__/ \_______/   \___/  
                                                                
         """)                                                       
global target
target = input("Enter company name: ")
print (target)
end = target.rsplit(".", 1)[-1]   

def main():
    options = [
    "[a] subdomain_enumeration", 
    "[b] technology_enumeration", 
    "[c] vulnerability_enumeration",
    "[d] exploit search",
    "[e] directory enumeration",
    "[f] ai analysis,"]
    terminal_menu = TerminalMenu(options, title="Options")
    menu_entry_index = terminal_menu.show()
    scripts = [
        "subdomains.py",
        "technology_enumeration.py", 
        "vulnerability_enumeration.py",
        "exploit_search.py",
        "directory_enumeration.py",
        "ai_analysis.py"
    ]


def subdomain_enum():
    print("Subdomain Enumeration Selected")
    os.system(f"nmap --script dns-brute-enum -sn -n {target} -oN {target}_dnsbrute")
    os.system(f"subfinder -d {target} -o {target}_subdomains")
    os.system(f"amass enum -d {target} -o {target}_amass")
    os.system(f"assetfinder --subs-only {target} >> {target}_subdomains")
def gobuster_sub():
    os.system(f"gobuster dns -d {target} -w ~/lst/sub_list -o {target}_gobuster -t 70 --wildcard")
    os.system(f"sed -i 's/www.//g' {target}_gobuster")
    os.system(f"sed -i 's/Found://g' {target}_gobuster")
    os.system(f"tail -n +11 {target}_gobuster >> {target}_clean")
    os.system(f"cat {target}_clean")
    os.system(f"mv -f {target}_clean {target}_file")
    os.system(f"sort -u {target}_subdomains -o {target}_subdomains")
    os.system(f"{target}_gobuster >> {target}_subdomains")
    os.system(f"sort -u {target}_subdomains -o {target}_subdomains")
    print(f"Subdomain enumeration completed. Results saved in {target}_subdomains")
subdomain_enum();
gobuster_sub();

def host_check():
            
            with open(f"{target}_subdomains") as f:
                subdomains = f.read().splitlines()
            live_subs = []
            for sub in subdomains:
                url = f".{sub}.com"
                try:
                    r = requests.get(url, timeout=15)
                    if r.status_code == 200:
                        print(f"[+] {url} is live")
                        live_subs.append(url)
                except requests.RequestException:
                    pass
            with open(f"{target}_live_subdomains.txt", "w") as f:
                for live in live_subs:
                    f.write(f"{live}\n")
            print(f"Live subdomains saved in {target}_live_subdomains.txt")
host_check();
#def option_2():
 #   print("Tech Enumeration")
  #  file = input("Enter file path")
   # os.system(f"sudo nmap sV --top-ports 30 -iL {target} -oN {target}_topportscan.txt -D RND:10 --data-length 20 --script auth")
   # print(f"Port scanning completed. Results saved in {target}_fullportscan.txt & {target}_topportscan.txt")