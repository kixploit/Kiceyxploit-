import os
import requests
import socket
import subprocess

# Warna
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
C = "\033[96m"
W = "\033[97m"

def banner():
    os.system('clear')
    print(f"""{G}
    ╔══════════════════════════╗
         {Y}KiceyXploit Tool{G} 
    ╚══════════════════════════╝
      Creator: {C}KiceyXploit
    """)

def ip_info():
    ip = input(f"{Y}[?]{W} Masukkan IP / Domain: ")
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        data = r.json()
        print(f"\n{G}[+] Hasil IP Info:")
        for key, value in data.items():
            print(f"{C}{key}{W}: {value}")
    except:
        print(f"{R}[!] Gagal mendapatkan data.")

def dns_lookup():
    domain = input(f"{Y}[?]{W} Masukkan domain: ")
    try:
        print(f"{G}[+] IP Address: {C}{socket.gethostbyname(domain)}")
    except:
        print(f"{R}[!] Domain tidak ditemukan.")

def whois_lookup():
    domain = input(f"{Y}[?]{W} Masukkan domain: ")
    try:
        result = subprocess.getoutput(f"whois {domain}")
        print(f"{G}[+] Hasil WHOIS:\n{W}{result}")
    except:
        print(f"{R}[!] Gagal WHOIS lookup.")

def port_scanner():
    target = input(f"{Y}[?]{W} Masukkan target IP: ")
    try:
        print(f"{G}[+] Scan port untuk {target} (1-100)...")
        for port in range(1, 101):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{C}Port {port} OPEN")
            sock.close()
    except:
        print(f"{R}[!] Error saat scan port.")

def auto_update():
    print(f"{Y}[+] Updating KiceyXploit...")
    os.system("git pull")

def menu():
    while True:
        banner()
        print(f"""
        {Y}[1]{W} IP Info
        {Y}[2]{W} DNS Lookup
        {Y}[3]{W} WHOIS Lookup
        {Y}[4]{W} Port Scanner
        {Y}[5]{W} Update Tool
        {Y}[6]{W} Exit
        """)
        choice = input(f"{Y}[?]{W} Pilih menu: ")
        if choice == "1":
            ip_info()
        elif choice == "2":
            dns_lookup()
        elif choice == "3":
            whois_lookup()
        elif choice == "4":
            port_scanner()
        elif choice == "5":
            auto_update()
        elif choice == "6":
            print(f"{G}Bye!{W}")
            break
        input(f"\n{C}[Enter]{W} untuk kembali ke menu...")

if __name__ == "__main__":
    menu()
