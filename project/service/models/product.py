from .common import BaseModel
from django.db import models

class Product(BaseModel):
    
    class Meta:
        verbose_name = '상품'
        verbose_name_plural = verbose_name+'들'
    
    name=models.CharField(
        verbose_name='상품 이름',
        max_length=100,
    )
    content=models.CharField(
        verbose_name='상품 내용',
        max_length=100,
    )
    sale_started_at=models.DateTimeField(
        verbose_name='판매 시작 시각',
        null=True,
        blank=True,
    )
    sale_ended_at=models.DateTimeField(
        verbose_name='판매 종료 시각',
        null=True,
        blank=True,
    )
    price=models.PositiveIntegerField(
        verbose_name='상품 금액',
        null=True,
        blank=True,
    )
    discount=models.PositiveIntegerField(
        verbose_name='할인 금액',
        null=True,
        blank=True,
    )
