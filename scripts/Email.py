import smtplib
import datetime

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'premisesgatenathan@gmail.com'
GMAIL_PASSWORD = '***********'

def sendmail( plate):
    headers = ["From: " + GMAIL_USERNAME, "Subject: Blocked Plate Detected" , "To: Nathan.James.Cusack@Gmail.com"]
    headers = "\r\n".join(headers)
    accessTime = datetime.datetime.now()
    HMS = accessTime.strftime("%H:%M:%S")
    DMY = accessTime.strftime("%d/%m/%Y")

    
    content = "A Blocked plate was detected at " + HMS + " on the "+ DMY +" Click this link to see the blocked plate: https://192.168.0.10/blocked"
    
    
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    
    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    
    session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)