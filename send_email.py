# For testing, you can hardcode first
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

smtp_server = "smtp.gmail.com"
port = 587
username = "brucewayne76211@gmail.com"
password = "your_app_password"

to_email = "srujangowda762@gmail.com"
subject = "Test Email"
body = "Hello! This is a test email from Python."

# Create message
msg = MIMEText(body, _charset="utf-8")
msg["From"] = username
msg["To"] = to_email
msg["Subject"] = subject
msg["Date"] = formatdate(localtime=True)  # Adds date header

# Send email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(username, [to_email], msg.as_string())

print("Email sent successfully!")


