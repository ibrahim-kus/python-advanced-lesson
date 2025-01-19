import smtplib
from email.mime.text import MIMEText

port = 587
smtp_server = "smtp-relay.brevo.com"
login = "83b387003@smtp-brevo.com"
password = ""


sender_email = ""
receiver_email = ""


text = """
    Merhaba, Bu eposta Python uygulamamdan gönderildi.
"""

message = MIMEText(text, "plain")
message["Subject"] = "Merhaba"
message["From"] = sender_email
message["To"] = receiver_email
# message["To"] = ",".join(email_list)

with smtplib.SMTP(smtp_server,port) as server:
    server.starttls()
    server.login(login,password)
    server.sendmail(sender_email,receiver_email,message.as_string())

print("Email send..")
