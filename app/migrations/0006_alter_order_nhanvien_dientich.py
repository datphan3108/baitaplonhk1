# Generated by Django 5.1.4 on 2024-12-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_order_nhanvien_thoigianbatdau_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_nhanvien',
            name='dientich',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
