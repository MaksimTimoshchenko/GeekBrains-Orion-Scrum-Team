# Generated by Django 4.0.2 on 2022-02-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_hub_id_post_hub_rename_user_id_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'DRAFT'), ('ACTIVE', 'ACTIVE'), ('DELETED', 'DELETED')], default='ACTIVE', max_length=16),
        ),
    ]