# Generated by Django 4.1.9 on 2023-07-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_registered_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='individual_organisation',
        ),
        migrations.AddField(
            model_name='registered',
            name='organisation_name',
            field=models.TextField(blank=True),
        ),
    ]