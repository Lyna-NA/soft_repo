# Generated by Django 3.1.7 on 2021-05-31 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_side', '0011_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, default='img/dogs/image2.jpeg', null=True, upload_to=''),
        ),
    ]