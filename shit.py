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



ef host_check():
            
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