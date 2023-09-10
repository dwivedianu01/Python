import smtplib
 
# list of email_id to send the mail
li = ["ps90046@gmail.com", "dwivedianu01@gmail.com"]
 
for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("dwivedijavaarchitect1983@gmail.com", "Sid!linux1981")
    message = "Python, Welcomes you....."
    s.sendmail("dwivedianu01@gmail.com", dest, message)
    s.quit()
