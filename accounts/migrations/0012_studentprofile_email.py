# Generated by Django 5.0.2 on 2024-02-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_document_status_alter_document_document_passport_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
