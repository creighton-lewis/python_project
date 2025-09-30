import os
import sys
import time
import subprocess
import random
from simple_term_menu import TerminalMenu


#import simple-term-menu

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
main();