import smtplib
import getpass
from email.mime.text import MIMEText


def send_mail():
    sender_address = 'redacted@gmail.com'
    password = getpass.getpass()
    subject = 'AI Mafia'
    msg = '''
            Hello World,
                This is a test mail
                FAF^@$*K)(*)*GS
                Thanking bot,
    '''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls( )
    server.login(sender_address, password)

    # drafting message
    msg = MIMEText(msg)
    msg['Subject'] = Subject
    msg['From'] = sender_address
    msg['To'] = 'redacted@gmail.com'
    recipients = 'redacted@gmail.com'

    server.sendmail(sender_address, msg.as_string())


send_mail()
