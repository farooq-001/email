import os
import psutil
import smtplib
import subprocess
from email.message import EmailMessage

# Configuration
DEVICE_NAME = "TEST-MISSION"  # Change The Device Name
DISK_THRESHOLD = 10  # Change The Percentage
MEMORY_THRESHOLD = 10  #Change The Percentage
RESOURCE_FILE = '/home/system_resource.txt'

EMAIL_CONFIG = {
    'sender': 'babafarooq001@gmail.com',
    'receivers': ['babafarooq001@gmail.com', 'babafarooq9154@gmail.com'],
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'username': 'babafarooq001@gmail.com',
    'password': 'glor fuby gbus rcal',
}

# Function to send email
def send_email(disk_alert, memory_alert):
    msg = EmailMessage()
    msg['From'] = EMAIL_CONFIG['sender']
    msg['To'] = ', '.join(EMAIL_CONFIG['receivers'])
    
    # Dynamic email subject
    if disk_alert:
        msg['Subject'] = f"{DEVICE_NAME} System Resource Alert: Disk space reached {DISK_THRESHOLD}%."
    elif memory_alert:
        msg['Subject'] = f"{DEVICE_NAME} System Resource Alert: Memory usage reached {MEMORY_THRESHOLD}%."
    
    # Email body
    body = f"System Resource Alert on {DEVICE_NAME}:\n\n"
    body += "System resource usage has exceeded the defined thresholds.\n"
    msg.set_content(body)
    
    # Attach the system resource file
    if os.path.exists(RESOURCE_FILE):
        with open(RESOURCE_FILE, 'rb') as f:
            msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=os.path.basename(RESOURCE_FILE))
    
    # Send the email
    try:
        with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
            server.starttls()
            server.login(EMAIL_CONFIG['username'], EMAIL_CONFIG['password'])
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to check system resources
def check_resources():
    disk_alert = False
    memory_alert = False

    # Check disk usage
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent >= DISK_THRESHOLD:
        disk_alert = True

    # Check memory usage
    memory = psutil.virtual_memory()
    if memory.percent >= MEMORY_THRESHOLD:
        memory_alert = True

    return disk_alert, memory_alert

# Main function
if __name__ == "__main__":
    disk_alert, memory_alert = check_resources()
    if disk_alert or memory_alert:
        # Generate the system resource report using subprocess
        try:
            command = "echo $USER && ifconfig | grep 172.31 | awk '{print $2}' && df -h && free -h"
            with open(RESOURCE_FILE, 'w') as file:
                subprocess.run(command, shell=True, stdout=file, stderr=subprocess.PIPE)
            print("System resource report generated successfully.")
        except Exception as e:
            print(f"Failed to generate system resource report: {e}")

        send_email(disk_alert, memory_alert)
