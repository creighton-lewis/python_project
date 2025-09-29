shit.code
global 
target=input("Enter the target domain (e.g., example.com): ")
print (target)
def intro_menu():
    print ("Welcome to the Reconnaissance Tool")
    print ("1. Subdomain Enumeration")
    print ("2. Port Scanning")
    print ("3. Directory Bruteforcing")
    print ("4. Exit")
    choice = input("Select an option (1-4): ")
    return choice


https://api.hunter.io/v2/companies/find?domain=hunter.io&api_key=a1d14852a2a6d291bede5c402cf0cd8779aa3f5a