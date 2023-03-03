from email.message import EmailMessage
import ssl
import smtplib
email_sender='sivaraj.win10@gmail.com'
email_password='yjvecrjjgcptuxaa'


sub='complaint registered'

def mail(email_reciever,body):
    em=EmailMessage()
    em['from']=email_sender
    em['to']=email_reciever
    em['subject']=sub
    em.set_content(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciever,em.as_string())

