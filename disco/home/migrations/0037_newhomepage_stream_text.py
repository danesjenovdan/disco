# Generated by Django 4.1.9 on 2023-10-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_newhomepage_stream_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='newhomepage',
            name='stream_text',
            field=models.TextField(blank=True),
        ),
    ]