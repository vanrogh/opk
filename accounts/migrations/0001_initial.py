# Generated by Django 4.1.5 on 2024-02-13 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('upload_086', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('upload_ent', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('parent1_name', models.CharField(max_length=100)),
                ('parent2_name', models.CharField(max_length=100)),
                ('parent1_phone', models.CharField(max_length=15)),
                ('certificate_of_good_conduct', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
