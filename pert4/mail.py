import smtplib
from email.message import EmailMessage


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'samandias88@gmail.com'
smtp_password = 'qsoh dpfo gjqt wzeu'

msg = EmailMessage()
msg['From'] = 'samandias88@gmail.com'
msg['To'] = 'junaedisamandias@gmail.com'
msg['Subject'] = 'Praktikum PJAR M4'
msg.set_content('Halo Selamat Sore \n Junaedi Samandias \n 50421706 \n 4IA11 \n Selamat Datang di Praktikum PJAR M4')

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username,smtp_password)
    smtp.send_message(msg)