# Generated by Django 4.1.9 on 2023-07-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_individualbyorganisation_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='vat_id',
            field=models.TextField(blank=True),
        ),
    ]
