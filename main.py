#Import relevant libraries
import os 
import socket 
import requests 
import random
from simple_term_menu import TerminalMenu#from rich.console import console
#Install necessary programs 

print("Welcome to Javelim")
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
    terminal_menu = TerminalMenu(options, title="options")
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
   # main()
    if menu_entry_index == 0:
        print ("option 1 selected")
        x=print(target)
        os.system("python3 subdomains.py {x}")
    elif menu_entry_index == 1:
        print ("option 2 selected")
        os.system("python3 tech.py {target}")
    elif menu_entry_index == 2:
        print ("option 3 selected")
        os.system("python3 vuln.py {target}")
    elif menu_entry_index == 3:
        print ("option 4 selected")
        os.system("python3 exploits.py {target}")
    elif menu_entry_index == 4:
        print ("option 5 selected")
        os.system("python3 dirb.py {target}")
    elif menu_entry_index == 5:
        print ("option 6 selected")
        os.system("python3 ai.py {target}")
if __name__ == "__main__":
    main()
