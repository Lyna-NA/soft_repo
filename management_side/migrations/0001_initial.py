# Generated by Django 3.2.4 on 2021-07-01 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('isbn', models.IntegerField()),
                ('title', models.CharField(default='', max_length=40)),
                ('language', models.CharField(default='', max_length=30)),
                ('bookPhoto', models.ImageField(default='', upload_to='bookPhoto/%Y/%m/%d/')),
                ('description', models.TextField(default='', max_length=400)),
                ('demurage', models.IntegerField(default=0)),
                ('author_name', models.CharField(default='', max_length=30)),
                ('version_number', models.CharField(default='', max_length=10)),
                ('year', models.DateField(default='', max_length=10)),
                ('condition', models.CharField(choices=[('bad', 'bad'), ('normal', 'normal'), ('good', 'good')], default='', max_length=40)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('delivered', 'delivered'), ('out of date', 'out of date'), ('available', 'available')], default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='person.png', null=True, upload_to='usersImages/%Y/%m/%d/')),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(default='', max_length=60, null=True)),
                ('city', models.CharField(default='', max_length=60, null=True)),
                ('state', models.CharField(default='', max_length=60, null=True)),
                ('street', models.CharField(default='', max_length=60, null=True)),
                ('building_num', models.CharField(default='', max_length=60, null=True)),
                ('dept_num', models.CharField(default='', max_length=60, null=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('phones', jsonfield.fields.JSONField(default=list)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('floor_id', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th')], max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('shelf_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_side.category')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='person.png', null=True, upload_to='usersImages/%Y/%m/%d/')),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(default='', max_length=60, null=True)),
                ('city', models.CharField(default='', max_length=60, null=True)),
                ('state', models.CharField(default='', max_length=60, null=True)),
                ('street', models.CharField(default='', max_length=60, null=True)),
                ('building_num', models.CharField(default='', max_length=60, null=True)),
                ('dept_num', models.CharField(default='', max_length=60, null=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('phones', jsonfield.fields.JSONField(default=list)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('working_floor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='management_side.floor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('issue_id', models.AutoField(default=4, primary_key=True, serialize=False)),
                ('issue_date', models.DateField(auto_now_add=True, null=True)),
                ('issue_for', models.DateField(default='', max_length=10)),
                ('last_edit', models.DateField(auto_now=True, null=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_side.book')),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='management_side.customer')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management_side.manager')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='floor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_side.floor'),
        ),
        migrations.CreateModel(
            name='BookPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_side.category')),
                ('floor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_side.floor')),
                ('shelf_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_side.shelf')),
            ],
            options={
                'unique_together': {('floor_id', 'shelf_id', 'cat_id')},
            },
        ),
        migrations.AddField(
            model_name='book',
            name='book_seat',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='management_side.bookposition'),
        ),
    ]
