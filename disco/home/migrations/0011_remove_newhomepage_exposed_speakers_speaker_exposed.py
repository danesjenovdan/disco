# Generated by Django 4.1.9 on 2023-07-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_newhomepage_exposed_speakers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newhomepage',
            name='exposed_speakers',
        ),
        migrations.AddField(
            model_name='speaker',
            name='exposed',
            field=models.BooleanField(default=False),
        ),
    ]
