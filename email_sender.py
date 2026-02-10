import smtplib
from email.message import EmailMessage
from secrets import sender_email, receiver_email, app_password


# Create email
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email from Python"
msg.set_content("Hello 👋\n\nThis email was sent using Python!")

# Send email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Error:", e)
