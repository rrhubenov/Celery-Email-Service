# Celery-Email-Service
A simple email service using Celery for asynchronous task execution. Should be paired with an event broker (for example RabbitMQ).

TO RUN:
Add a system environment variable for the sender email ('EMAIL_USER') and the email password ('EMAIL_PASSWORD').
run 'celery -A email_service worker --loglevel=info' in the terminal to start the Celery worker.
