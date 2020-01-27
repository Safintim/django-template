from django.contrib.auth.models import AbstractUser
from django.db import models

from rest_framework.authtoken.models import Token


class User(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=11, unique=True)
    username = models.CharField(max_length=300, blank=True, null=True)
    email = models.CharField('Email', max_length=300, blank=True, null=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return self.phone

    def save(self, **kwargs):
        super().save(**kwargs)
        if not self.is_active:
            Token.objects.filter(user=self).delete()
