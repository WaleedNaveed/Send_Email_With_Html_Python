# Importing the required modules
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender email id and password
admin_email_id = "sender@gmail.com"
admin_email_id_password = "Sender@gmail.comPassword"

# Receivers email ids
subscribers_email_ids_list = ["xyz@gmail.com", "abc@hotmail.com"] 

# Creating MIMEMultipart message because we have to send both text and html in email
email_message = MIMEMultipart("alternative")

# This will be the email subject
email_subject = "Email Subject"

# Creating the plain text and html forms of the email
email_body_plain_text = """\
Hi,
Kindly visit cricinfo for any updates regarding cricket, here is the link
https://www.espncricinfo.com/"""
email_body_html = """\
<html>
  <body>
    <p>Hi,<br>
       Kindly visit cricinfo for any updates regarding cricket, here is the link<br>
       <a href="https://www.espncricinfo.com/">Cricinfo</a> 
    </p>
  </body>
</html>
"""

email_message["Subject"] = email_subject

#Converting the plain text and html created above to the required MIME type
plain_text = MIMEText(email_body_plain_text, "plain")
html_text = MIMEText(email_body_html, "html")

# Adding both text and html parts to the email. Reason for adding both is that there are some email clients who do not allow html.
# Email clients render the last part, so if the client does not allow html then plain text will be displayed else html will be displayed
email_message.attach(plain_text)
email_message.attach(html_text)
  
# Using gmail SMTP. Creating SMTP session 
smtp_session = smtplib.SMTP('smtp.gmail.com', 587) 
  
# Starting TLS for security 
smtp_session.starttls() 
  
# Authenticating
smtp_session.login(admin_email_id, admin_email_id_password) 
  
print('Sending emails')

# Loop on list of receivers emails to send the email to all receivers
for email_id in subscribers_email_ids_list:
    smtp_session.sendmail(admin_email_id, email_id, email_message.as_string())
	
print('Successfully sent emails to all receivers')  

# closing the SMTP session 
smtp_session.quit() 