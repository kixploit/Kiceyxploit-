#!/bin/bash
clear
echo "Installing KiceyXploit..."
pkg update -y
pkg install python git curl -y
pip install requests
echo "Installation Complete!"
echo "Run tool dengan: python kiceyxploit.py"
