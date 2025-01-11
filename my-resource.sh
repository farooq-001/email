#!/bin/bash

# Check the OS distribution dynamically
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo "Unable to detect the Linux distribution."
    exit 1
fi

# Install Python 3 and pip3 dynamically
if command -v apt-get &> /dev/null; then
    sudo apt update
    sudo apt install python3 python3-pip -y
elif command -v yum &> /dev/null; then
    sudo yum install python3 python3-pip -y
elif command -v dnf &> /dev/null; then
    sudo dnf install python3 python3-pip -y
elif command -v pacman &> /dev/null; then
    sudo pacman -Syu python python-pip --noconfirm
else
    echo "Package manager not found. Please install Python manually."
    exit 1
fi

# Install required Python packages
sudo pip3 install psutil smtplib

# Clone the repository
git clone https://github.com/farooq-001/email.git

# Run the Python script
sudo python3 email/resource_alert.py

# Clean up by removing the cloned directory
sudo rm -rf email
