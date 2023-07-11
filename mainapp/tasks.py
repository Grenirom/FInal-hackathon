from account.send_mail import send_activation_mail
from .celery import app


@app.task
def send_activation_mail_task(user, code):
    send_activation_mail(user, code)
