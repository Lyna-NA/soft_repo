# Generated by Django 3.1.7 on 2021-05-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_side', '0014_auto_20210531_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, default='person.png', null=True, upload_to=''),
        ),
    ]
