import os
import nmap
import sys
import time
import subprocess
import random
from simple_term_menu import TerminalMenu


#import simple-term-menu

print("""\
      /$$$$$$                                /$$             /$$    
 /$$__  $$                              | $$            | $$    
| $$  \__/  /$$$$$$$  /$$$$$$   /$$$$$$ | $$  /$$$$$$  /$$$$$$  
|  $$$$$$  /$$_____/ |____  $$ /$$__  $$| $$ /$$__  $$|_  $$_/  
 \____  $$| $$        /$$$$$$$| $$  \__/| $$| $$$$$$$$  | $$    
 /$$  \ $$| $$       /$$__  $$| $$      | $$| $$_____/  | $$ /$$
|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$      | $$|  $$$$$$$  |  $$$$/
 \______/  \_______/ \_______/|__/      |__/ \_______/   \___/  
                                                                
         """)                                                       
                                                            

def main():
    options = [
    "[a] subdomain_enumeration", 
    "[b] technology_enumeration", 
    "[o] vulnerability_enumeration"]
    terminal_menu = TerminalMenu(options, title="Options")
    menu_entry_index = terminal_menu.show()


if __name__ == "__main__":
    main()
