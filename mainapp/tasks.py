from account.send_mail import send_activation_mail
from orders.send_conf_email import send_order_confirm
from .celery import app


@app.task
def send_activation_mail_task(user, code):
    send_activation_mail(user, code)


@app.task
def send_order_confirm_email(user, code):
    send_order_confirm(user, code)
