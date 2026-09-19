import smtplib 
from email.message import EmailMessage

# message with Subject and attachments
sender = 'rakkeshadithya00@gmail.com' 
password = 'nkifyatdplejfiux'
message = EmailMessage()
message['From'] = 'rakkeshadithya00@gmail.com'
message['To'] = 'rakkeshadithya00@gmail.com'
message['Subject'] = 'HOMEWORK'
files = ['day31.py']
for filename in files:
    with open(filename, 'rb') as f:
        file_data = f.read() 
        message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password) 
    conn.send_message(message)
print('Message sent successfully')

