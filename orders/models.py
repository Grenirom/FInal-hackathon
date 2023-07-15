from django.contrib.auth import get_user_model
from django.db import models
from comics.models import Comics

User = get_user_model()

STATUS_CHOICES = (
    ('open', 'Открыт'),
    ('in_process', 'В обработке'),
    ('closed', 'Закрыт'),
)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    comics = models.ForeignKey(Comics, related_name='orders', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    order_confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    confirm_code = models.CharField(max_length=222, default='', null=True, blank=True)

    def create_confirm_code(self):
        from uuid import uuid4
        code = str(uuid4())
        self.confirm_code = code
