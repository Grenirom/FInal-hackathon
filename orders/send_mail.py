from django.core.mail import send_mail


def send_notification_task(user, order_id, price):
    send_mail(
        'Уведомление о создании заказа!',
        f'''Вы создали заказ №{order_id},ожидайте звонка!
        Полная стоимость вашего заказа:{price}.
        Спасибо за то что выбрали нас!''',
        'from@example.com',
        [user],
        fail_silently=False
    )
