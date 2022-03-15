import smtplib as mail

server = mail.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login('devansh151005@gmail.com', 'Omdevansh1424')
server.sendmail('devansh151005@gmail.com',
                'devansh151005@icloud.com',
                'Yo Cool dude how are you? ')
