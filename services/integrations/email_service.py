"""
===============================================================================
File Name : email_service.py
Purpose   : Enterprise Email Service
===============================================================================
"""
import traceback
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailService:

    def __init__(self):

        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.report_email = os.getenv("REPORT_EMAIL")

        print("=" * 60)
        print("SMTP_SERVER   :", self.smtp_server)
        print("SMTP_PORT     :", self.smtp_port)
        print("EMAIL_USER    :", self.email_user)
        print("REPORT_EMAIL  :", self.report_email)
        print("PASSWORD      :", "Loaded" if self.email_password else "Not Loaded")
        print("=" * 60)

    # ------------------------------------------------------------------

    def send_email(self, to_email, subject, body):

        try:

            msg = MIMEMultipart()

            msg["From"] = self.email_user
            msg["To"] = self.report_email
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:

                server.starttls()

                server.login(self.email_user, self.email_password)

                server.send_message(msg)

            print("Email sent successfully.")

            return True


        except Exception as e:

            print("\nFULL ERROR")

            print("=" * 60)

            traceback.print_exc()

            print("=" * 60)

            print(e)

            return False