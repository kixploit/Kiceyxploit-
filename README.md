# 🔥 KiceyXploit Tool 🔥

KiceyXploit adalah tools informasi & pentesting ringan untuk Termux dan Linux, dibuat untuk mempermudah pengumpulan informasi awal (recon) dan scanning target.  
Creator: **KiceyXploit**  

---

## ✨ Fitur Utama
✔ IP Info (Dapatkan detail IP/Domain)  
✔ DNS Lookup  
✔ WHOIS Lookup  
✔ Port Scanner (1–100)  
✔ Auto Update  

---

## 📥 Cara Install
```bash
pkg update && pkg upgrade -y
pkg install git python whois -y
pip install requests
git clone https://github.com/KiceyXploit/KiceyXploit.git
cd KiceyXploit
bash install.sh
python kiceyxploit.py
