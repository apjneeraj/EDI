import smtplib, subprocess, os

#subprocess.call('./Systeminfo.shSystemlog.txt')
os.system('bash ./Systeminfo.sh > Systemlog.txt')
conn=smtplib.SMTP_SSL('smtp.googlemail.com',465)
conn.login('apj.mishra@gmail.com','')

fopen=open("Systemlog.txt")
text=fopen.read()
fopen.close()
os.remove('Systemlog.txt')


'''Message = """From: WDCloud <apj.mishra@gmail.com>
To: Neeraj <apjneeraj@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""+text.strip()'''

Message='Subject:WD Hourly Cloud Stats\n\n' + text.strip()

conn.sendmail('Neeraj Mishra<apjmishra@gmail.com>','apjneeraj@gmail.com',Message)

conn.quit()


