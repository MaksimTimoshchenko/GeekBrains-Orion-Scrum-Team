# Generated by Django 4.0.2 on 2022-03-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_banned',
            field=models.BooleanField(default=False, verbose_name='Заблокирован'),
        ),
    ]