# Generated by Django 4.1.9 on 2023-07-09 10:02

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_speaker_programmeday'),
    ]

    operations = [
        migrations.AddField(
            model_name='newhomepage',
            name='exposed_speakers',
            field=wagtail.fields.StreamField([('speaker', wagtail.blocks.ChoiceBlock(choices=[(1, 'Shoshana Zuboff')]))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AddField(
            model_name='newspage',
            name='speaker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.speaker'),
        ),
    ]
