#!/bin/bash

# Install Python 3 and pip3
sudo apt install python3 -y
sudo apt install python3-pip -y

# Install required Python packages
sudo pip3 install psutil smtplib

# Clone the repository
sudo git clone https://github.com/farooq-001/emil.git

# Run the Python script
sudo python3 email/resource_alert.py

# Clean up by removing the cloned directory
sudo rm -rf email
