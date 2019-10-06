from celery import Celery
import smtplib, ssl
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

port = 465

context = ssl.create_default_context()

app = Celery("email_service", broker="amqp://localhost")

@app.task
def sendEmail(reciever_email):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, reciever_email, "Lorem Ipsum")