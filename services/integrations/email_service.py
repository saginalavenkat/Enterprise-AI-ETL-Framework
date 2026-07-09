"""
===============================================================================
File Name : email_service.py
Purpose   : Enterprise Email Service
===============================================================================
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from core.config import (SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASSWORD)


class EmailService:

    def send_email(self, to_email, subject, body):

        msg = MIMEMultipart()

        msg["From"] = EMAIL_USER
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

            server.starttls()

            server.login(EMAIL_USER, EMAIL_PASSWORD)

            server.send_message(msg)

        return True