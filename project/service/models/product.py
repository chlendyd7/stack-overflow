from .common import BaseModel
from django.db import models

class Product(BaseModel):
    
    class Meta:
        verbose_name = '상품'
        verbose_name_plural = verbose_name
    
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
    category=models.ManyToManyField(
        to='Category',
        through='ProductCategory'
    )


class ProductImage(BaseModel):
    class Meta:
        verbose_name='상품 이미지',
        verbose_name_plural = verbose_name
        ordering = ('order',)

    product=models.ForeignKey(
        to='Product',
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        upload_to='product',
        width_field='width',
        height_field='height',
        null=True,
        blank=True,
    )
    image_link = models.URLField(
        max_length=400,
        null=True,
        blank=True,
    )
    width = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    height = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    order = models.PositiveIntegerField(
        default=1,
        verbose_name='순서'
    )
    start_at = models.DateTimeField(
        verbose_name='노출 시작 일시',
        null=True,
        blank=True,
    )
    end_at = models.DateTimeField(
        verbose_name='노출 종료 일시',
        null=True,
        blank=True,
    )


class Category(BaseModel):
    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = verbose_name

    name = models.CharField(
        verbose_name='이름',
        max_length=64,
    )

    def __str__(self):
        return self.name


class ProductCategory(BaseModel):
    class Meta:
        verbose_name = '상품, 카테고리 관계 테이블'

    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)

class Stock(models.Model):
    class Meta:
        verbose_name = '상품재고'

    prodcut=models.OneToOneField(to='Product', on_delete=models.CASCADE)
    amount=models.IntegerField(
        verbose_name='재고 양',
        default=0,
        null=True,
        blank=True
    )
