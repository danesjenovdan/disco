# Generated by Django 4.1.9 on 2023-07-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_registeredspeaker'),
    ]

    operations = [
        migrations.AddField(
            model_name='newhomepage',
            name='speaker_application_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='newhomepage',
            name='speaker_application_title',
            field=models.TextField(blank=True),
        ),
    ]