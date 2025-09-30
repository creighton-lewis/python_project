#Install necessary libraries 
import requests 
import os 
import * from main
options = [ "single domain" , "multiple domains"]
from simple_term_menu import TerminalMenu
terminal_menu = TerminalMenu(options, title="Options")
menu_entry_index = terminal_menu.show()
options = options[menu_entry_index]

if options == "single domain":
    print(target)
    target = input("Enter the target domain (e.g., example.com): ")
    os.system(f"nuclei -u {target} -as -o {target}_nuclei -vv --stats")
    os.system(f"nmap -sV -sU --script=auth,vuln {target} --top-ports 50 -oN {target}_nmap -D RND:5 --reason -Pn")
elif options == "multiple domains":
    target = input("Enter the file name containing the list of domains (e.g., domains.txt): ")  
    os.system(f"nuclei -list {target} -as -o bulk_nuclei_results.txt")
    os.system(f"nmap -sV -sU --script=auth -iL {target} --top-ports 50 -oN -D RND:5 --reason -Pn")


