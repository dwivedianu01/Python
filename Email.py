import smtplib
 
# list of email_id to send the mail
li = ["py1@gmail.com", "xyz1@gmail.com"]
 
for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("xyz@gmail.com", "password")
    message = "Python, Welcomes you....."
    s.sendmail("xyz1@gmail.com", dest, message)
    s.quit()
