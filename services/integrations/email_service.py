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
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.logger.logger import logger

class EmailService:

    def __init__(self):

        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.report_email = os.getenv("REPORT_EMAIL", self.email_user)

        print("=" * 60)
        print("SMTP_SERVER   :", self.smtp_server)
        print("SMTP_PORT     :", self.smtp_port)
        print("EMAIL_USER    :", self.email_user)
        print("REPORT_EMAIL  :", self.report_email)
        print("PASSWORD      :", "Loaded" if self.email_password else "Not Loaded")
        print("=" * 60)

    # ------------------------------------------------------------------

    def send_email(self, to_email, subject, body, attachments=None, monitor=None):

        try:

            to_email = to_email or self.report_email

            if not to_email:
                print("REPORT_EMAIL is not configured.")
                return False

            msg = MIMEMultipart()

            msg["From"] = self.email_user
            msg["To"] = to_email
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "plain"))

            # -----------------------------------------
            # Attach files
            # -----------------------------------------

            if attachments:

                logger.info("=" * 60)
                logger.info("Email Attachments")
                logger.info("=" * 60)

                for file_path in attachments:

                    logger.info(f"Attaching : {file_path}")

                    if os.path.exists(file_path):

                        with open(file_path, "rb") as attachment:

                            part = MIMEBase("application", "octet-stream")

                            part.set_payload(attachment.read())

                        encoders.encode_base64(part)

                        part.add_header(
                            "Content-Disposition",
                            f'attachment; filename="{os.path.basename(file_path)}"'
                        )

                        msg.attach(part)

                    else:

                        logger.warning(f"Attachment not found : {file_path}")

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:

                server.starttls()

                server.login(self.email_user, self.email_password)

                server.send_message(msg)

            print("Email sent successfully.")

            if monitor:
                monitor.email_sent()

            return True

        except Exception:

            traceback.print_exc()

            return False