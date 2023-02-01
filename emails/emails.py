import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

user = ''
pw = ''

html = Template(Path('emails/index.html').read_text())
email = EmailMessage()
email['from'] = 'x@x.de'
email['to'] = 'x@z.de'
email['subject'] = 'Test'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='mail.gmx.net', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user, pw)
    smtp.send_message(email)
    print('all good')
