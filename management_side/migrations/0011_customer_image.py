# Generated by Django 3.1.7 on 2021-05-31 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_side', '0010_auto_20210530_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
