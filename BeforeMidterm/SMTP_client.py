import smtplib

message = """From: From Joe <joe@blow.com>
To: To Herny <s6506022620095@email.kmutnb.ac.th>
MIME-Version: 1.0
Content-type: text/html
Subject: Test Email

This is a test email.
<b>This is bold</b>
<h1>Test Email</h1>
"""

try:
    smtp = smtplib.SMTP("192.168.1.124")
    smtp.sendmail("s6506022620095@email.kmutnb.ac.th", message)
except Exception as err:
    print(str(err))