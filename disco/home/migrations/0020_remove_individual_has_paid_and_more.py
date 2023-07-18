# Generated by Django 4.1.9 on 2023-07-18 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_organisation_vat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='has_paid',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='has_paid',
        ),
        migrations.AddField(
            model_name='individualbyorganisation',
            name='mautic_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='is_participant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registered',
            name='has_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registered',
            name='mautic_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='individualbyorganisation',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='individualbyorganisation',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='individuals', to='home.organisation'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='vat_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]
