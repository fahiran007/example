# Generated by Django 4.0.6 on 2022-09-04 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nickName', models.CharField(max_length=50)),
                ('Birthyear', models.CharField(max_length=50)),
                ('Bestfriend', models.CharField(max_length=50)),
                ('Hobby', models.CharField(max_length=50)),
            ],
        ),
    ]