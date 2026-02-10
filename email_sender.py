import smtplib
from email.message import EmailMessage
from secrets import sender_email, receiver_email, app_password

def send_email(receiver_email: str, Subject: str, content: str) -> str:
    """send an email using the provided receiver_email, Subject and content"""
    # Create email
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = Subject
    msg.set_content(content)
    
    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
    print("✅ Email sent successfully!")
    return "Email sent successfully!"
