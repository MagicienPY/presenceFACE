# Generated by Django 3.2.16 on 2023-01-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='caption',
            field=models.CharField(default='non', max_length=200),
            preserve_default=False,
        ),
    ]