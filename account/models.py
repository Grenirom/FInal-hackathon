from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_rest_passwordreset.signals import reset_password_token_created

from account.managers import MyCustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_("email"), unique=True)
    first_name = models.CharField(_("first_name"), max_length=150)
    last_name = models.CharField(_("last_name"), max_length=150)
    password = models.CharField(max_length=129)
    activation_code = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='images', blank=True, default='images/marvel-default.jpg')
    is_active = models.BooleanField(_("active"), default=False)
    is_staff = models.BooleanField(_("staff status"), default=False)
    username = models.CharField(_("username"), max_length=100)

    objects = MyCustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def create_code_for_activation(self):
        code = str(uuid4())
        self.activation_code = code


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        'Восстановление пароля marvel аккаунта',
        # message:
        email_plaintext_message,
        # from:
        "marvel.fullstack@gmail.com",
        # to:
        [reset_password_token.user.email]
    )