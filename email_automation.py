'''
SMTP(simple mail Transfer protocol)
-----------------------------------
--> this is used to send emails from server to another...

NOTE:
----
1. SMTP SSL Port
----------------
465
2.SMTP TLS port
---------------
587

import smtplib

Email Message Class
-------------------
msg ['sudject'] = 'SMTP ON Mail'
msg ['From'] = 'sneder@mail.com'
msg ['To'] = 'Receiver@mail.com'
vemk gwih nrqd tifa

'''
'''
import smtplib
from email.message import EmailMessage
sender = 'dasarichandrasekhar23@gmail.com'
password = 'vemk gwih nrqd tifa'
msg =  EmailMessage()
msg['subject'] = 'panii kii  maalinaa  maill ra puavu edhii'
msg['from'] = sender
msg['To'] = 'dasaritulasirao0@gmail.com'
msg.set_content('haii papap ghfkvnbvgkuygn guygnbblhjbmnbi jbjj,mnk hfkjfsdkjbcbm ibfldsbvmnzzlkca mdn xbajdsmbnvlbaokjbfdnsbckj berbajvbnmsdaolsedlnm bfdjblssl')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()
'''
import smtplib
from email.message import EmailMessage
sender = 'dasarichandrasekhar23@gmail.com'
password = 'vemk gwih nrqd tifa'
msg =  EmailMessage()
reveriers =['dasaritulasirao0@gmail.com','dasarichandrasekhar88@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in reveriers:
    msg['subject'] = 'panii kii  maalinaa  maill ra puavu edhii'
    msg['from'] = sender
    msg['To'] = email
    msg.set_content('haii papap ghfkvnbvgkuygn guygnbblhjbmnbi jbjj,mnk hfkjfsdkjbcbm ibfldsbvmnzzlkca mdn xbajdsmbnvlbaokjbfdnsbckj')
    server.send_message(msg)
server.quit()





