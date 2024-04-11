import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = verbose_name
    
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    nickname = models.CharField(
        max_length=100,
        verbose_name='닉네임',
        null=True,
    )
    phone_number = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=10,
        verbose_name='성별',
        null=True,
        blank=True,
    )
    removed_at = models.DateTimeField(
        null=True,
        blank=True,
    )
