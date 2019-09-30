from celery import Celery

app = Celery("email_service", broker="amqp://localhost")