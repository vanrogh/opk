# Generated by Django 4.1.5 on 2024-02-14 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_studentprofile_certificate_ent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentProfile',
        ),
    ]