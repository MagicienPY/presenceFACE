# Generated by Django 3.2.16 on 2023-01-22 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_uploadimage_caption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimage',
            old_name='caption',
            new_name='Nom',
        ),
    ]