import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def run_tests_and_send_email():
    # Run Pytest tests
    subprocess.run(["pytest", "-s", "-v"])

    # Path to the generated report.html file
    report_path = '.report/report.html'

    # Recipient email addresses
    recipient_emails = ['touhidul_islam@example', 'recipient2@example.com']

    # Email configuration
    email_subject = 'Test Report'
    email_body = 'Please find attached the test report.'

    # Set up the SMTP server
    smtp_server = "your_smtp_server"
    smtp_port = 587
    smtp_username = "your_email@example.com"
    smtp_password = "your_email_password"

    # Create a message object
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = ', '.join(recipient_emails)
    msg['Subject'] = email_subject

    # Attach the HTML report
    with open(report_path, 'rb') as file:
        attach = MIMEApplication(file.read(), _subtype="html")
        attach.add_header('Content-Disposition', 'attachment', filename='report.html')
        msg.attach(attach)

    # Attach the email body as plain text
    msg.attach(MIMEText(email_body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(smtp_username, recipient_emails, msg.as_string())

    # Disconnect from the SMTP server
    server.quit()


if __name__ == "__main__":
    run_tests_and_send_email()
