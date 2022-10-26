# ------------- FOR PRODUCTION -------------
# import os
# import smtplib

# e_addr = os.environ.get('MAIL_ADDRESS')
# e_pwd = os.environ.get('GMAIL_APP_PWD')

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#   smtp.ehlo()
#   smtp.starttls() # to encrypt traffic
#   smtp.ehlo()
  
#   smtp.login(e_addr, e_pwd) # to login to mail server
  
#   subj = 'Test email'
#   body = 'Hello dear Usman Musa'
  
#   msg = f"Subject: {subj}\n\n{body}"
#   smtp.sendmail(e_addr, 'usmanmusa1920@gmail.com', msg)
# ---------------------------------------------------------
  
  
  
  
# ------------- FOR LOCAL ------------- it work
# first run the python email server on terminal by:
#     python3 -m smtpd -c DebuggingServer -n localhost:1025
# import smtplib

# e_addr = os.environ.get('MAIL_ADDRESS')

# with smtplib.SMTP('localhost', 1025) as smtp:
  
#   subj = 'Test email'
#   body = 'Hello dear Usman Musa'
  
#   msg = f"Subject: {subj}\n\n{body}"
  
#   smtp.sendmail(e_addr, 'usmanmusa1920@gmail.com', msg)
# ---------------------------------------------------------
  
  
  
  
# ------------- FOR SSL ------------- it work
# import os
# import smtplib

# e_addr = os.environ.get('MAIL_ADDRESS')
# e_pwd = os.environ.get('GMAIL_APP_PWD')

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  
#   smtp.login(e_addr, e_pwd)
  
#   subj = 'Test email'
#   body = 'Hello dear Usman Musa'
  
#   msg = f"Subject: {subj}\n\n{body}"
  
#   smtp.sendmail(e_addr, 'usmanmusa1920@gmail.com', msg)
# ---------------------------------------------------------
  
  
  
  
# ------------- FOR EMAIL MESSAGE OBJECT TO SEND MESSAGE ------------- it work
# import os
# import smtplib
# from email.message import EmailMessage

# e_addr = os.environ.get('MAIL_ADDRESS')
# e_pwd = os.environ.get('GMAIL_APP_PWD')

# msg = EmailMessage()
# msg['Subject'] = 'Test email'
# msg['From'] = e_addr
# msg['To'] = os.environ.get('MAIL_ADDRESS')
# msg.set_content('Hello dear Usman Musa')

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#   smtp.login(e_addr, e_pwd)
  
#   smtp.send_message(msg)
# ---------------------------------------------------------
  
  
  
  
# ------------- FOR ONE IMAGE ATTACHMENT -------------
# import os
# import smtplib
# import imghdr
# from email.message import EmailMessage

# e_addr = os.environ.get('MAIL_ADDRESS')
# e_pwd = os.environ.get('GMAIL_APP_PWD')

# msg = EmailMessage()
# msg['Subject'] = 'Attachment'
# msg['From'] = e_addr
# msg['To'] = os.environ.get('MAIL_ADDRESS')
# msg.set_content('Hello dear Usman Musa')

# with open('image.png', 'rb') as i:
#   img = i.read()
#   f_type = imghdr.what(i.name)
#   f_name = i.name
  
# msg.add_attachment(img, maintype='image', subtype=f_type, filename=f_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#   smtp.login(e_addr, e_pwd)
  
#   smtp.send_message(msg)
# ---------------------------------------------------------
  
  
  
  
# ------------- FOR MULTIPLE IMAGE ATTACHMENT -------------
# import os
# import smtplib
# import imghdr
# from email.message import EmailMessage

# e_addr = os.environ.get('MAIL_ADDRESS')
# e_pwd = os.environ.get('GMAIL_APP_PWD')

# msg = EmailMessage()
# msg['Subject'] = 'Attachment'
# msg['From'] = e_addr
# msg['To'] = os.environ.get('MAIL_ADDRESS')
# msg.set_content('Hello dear Usman Musa')

# images = ['image_1.jpg', 'image_2.jpg', 'image_3.jpg', 'image_4.jpg']
# for my_img in images:
  # with open(my_img, 'rb') as i:
  #   img = i.read()
  #   f_type = imghdr.what(i.name)
  #   f_name = i.name
    
  # msg.add_attachment(img, maintype='image', subtype=f_type, filename=f_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#   smtp.login(e_addr, e_pwd)
  
#   smtp.send_message(msg)
# ---------------------------------------------------------
  
  
  
  
# ------------- FOR SENDING PDF ATTACHMENT -------------
# import os
# import smtplib
# from email.message import EmailMessage

# e_addr = os.environ.get('MAIL_ADDRESS')
# e_pwd = os.environ.get('GMAIL_APP_PWD')

# msg = EmailMessage()
# msg['Subject'] = 'Attachment'
# msg['From'] = e_addr
# msg['To'] = os.environ.get('MAIL_ADDRESS')
# msg.set_content('Hello dear Usman Musa')

# images = ['my_docs.pdf']
# for my_pdf in images:
  # with open(my_pdf, 'rb') as i:
  #   img = i.read()
  #   f_name = i.name
    
  # msg.add_attachment(img, maintype='application', subtype='octet-stream', filename=f_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#   smtp.login(e_addr, e_pwd)
  
#   smtp.send_message(msg)
# ---------------------------------------------------------
  
  
  
  
# ------------- FOR SENDING MAIL TO MULTIPLE PEOPLE -------------
# import os
# import smtplib
# from email.message import EmailMessage

# e_addr = os.environ.get('MAIL_ADDRESS')
# e_pwd = os.environ.get('GMAIL_APP_PWD')

# people_email = ['person_1@gmail.com', 'person_2@gmail.com', 'person_3@gmail.com']

# msg = EmailMessage()
# msg['Subject'] = 'Attachment'
# msg['From'] = e_addr
# msg['To'] = ', '.join(people_email)
# msg.set_content('Hello dear Usman Musa')

# images = ['my_docs.pdf']
# for my_pdf in images:
  # with open(my_pdf, 'rb') as i:
  #   img = i.read()
  #   f_name = i.name
    
  # msg.add_attachment(img, maintype='application', subtype='octet-stream', filename=f_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#   smtp.login(e_addr, e_pwd)
  
#   smtp.send_message(msg)
# ---------------------------------------------------------
  
  
  
  
# ------------- FOR SENDING HTML MESSAGE ------------- it work
import os
import smtplib
from email.message import EmailMessage

e_addr = os.environ.get('MAIL_ADDRESS')
e_pwd = os.environ.get('GMAIL_APP_PWD')

contacts = ['person_1@gmail.com', 'person_2@gmail.com', 'person_3@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'My email subject!'
msg['From'] = e_addr
msg['To'] = os.environ.get('MAIL_ADDRESS')

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">Hello world email address!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(e_addr, e_pwd)
    smtp.send_message(msg)
# ---------------------------------------------------------
