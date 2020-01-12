# Generated by Django 2.1.7 on 2020-01-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinyurls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tinyurl',
            name='last_used_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tinyurl',
            name='expires_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]