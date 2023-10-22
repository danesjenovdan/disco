# Generated by Django 4.1.9 on 2023-10-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_alter_programmeday_timeslots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered',
            name='registration_fee',
            field=models.IntegerField(blank=True, choices=[(50, '€50 plus VAT (€54.75 total)'), (25, '€25 plus VAT or €27.37 in total (for those unable to afford the standard fee)'), (75, '€75 plus VAT or €82.13 in total (for those who want to support participants with subsidised fee)')], null=True),
        ),
    ]