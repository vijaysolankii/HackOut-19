# Generated by Django 2.2.1 on 2019-07-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_chat_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taken',
            name='email',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='taken',
            name='username',
            field=models.CharField(default='', max_length=250),
        ),
    ]