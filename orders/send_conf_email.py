from django.core.mail import send_mail

HOST = 'localhost:3000'


def send_order_confirm(email, code):
    full_link = f'http://{HOST}/orders/confirm/{code}/'
    send_mail(
        'Вас приветствует Marvel-Fullstack!',
        'Для подтверждения вашего заказа вам необходимо перейти по ссылке:'
        f'\n{full_link}',
        'marvel.fullstack@gmail.com',
        [email]
    )
