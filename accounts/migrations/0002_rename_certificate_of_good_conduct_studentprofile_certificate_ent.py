# Generated by Django 4.1.5 on 2024-02-13 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='certificate_of_good_conduct',
            new_name='certificate_ent',
        ),
    ]