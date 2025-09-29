simple_menu.py
from consolemenu import *
from consolemenuitems import * 
menu = ConsoleMenu ("Title", "Subtitle")
menu_item=MenuItem("Menu Item")
function_item = FunctionItem("Call function", input, ["Enter an input"])