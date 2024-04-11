# Generated by Django 4.2.11 on 2024-04-11 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '상품', 'verbose_name_plural': '상품'},
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 일시')),
                ('removed_at', models.DateTimeField(blank=True, null=True, verbose_name='삭제 일시')),
                ('image', models.ImageField(blank=True, height_field='height', null=True, upload_to='product', width_field='width')),
                ('image_link', models.URLField(blank=True, max_length=400, null=True)),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=1, verbose_name='순서')),
                ('start_at', models.DateTimeField(blank=True, null=True, verbose_name='노출 시작 일시')),
                ('end_at', models.DateTimeField(blank=True, null=True, verbose_name='노출 종료 일시')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='service.product')),
            ],
            options={
                'verbose_name': ('상품 이미지',),
                'verbose_name_plural': ('상품 이미지',),
                'ordering': ('order',),
            },
        ),
    ]
