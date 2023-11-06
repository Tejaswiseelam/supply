#!/usr/bin/env python

import cgi
import smtplib

form = cgi.FieldStorage()

if "email" in form:
    email = form["email"].value
    print("Content-type: text/html\n")
    print("Thank you! Check your email for a confirmation.")

def send_thank_you_email(email):
    # Code to send a thank you email using smtplib
    # Replace placeholder values with your email server details
    smtp_server = "smtp.yourserver.com"
    port = 587
    sender_email = "YOUR_EMAIL_ADDRESS"
    password = "YOUR_PASSWORD"

    message = "Subject: Thank You for Your Donation\n\nDear User, Thank you for your donation!"

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message)

