# Generated by Django 4.1.5 on 2024-02-20 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
