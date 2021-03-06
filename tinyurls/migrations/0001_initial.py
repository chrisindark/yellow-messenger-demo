# Generated by Django 2.1.7 on 2020-01-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TinyUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tiny_id', models.CharField(db_index=True, max_length=10)),
                ('original_url', models.URLField()),
                ('expires_on', models.DateTimeField(blank=True, null=True)),
                ('last_used_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
