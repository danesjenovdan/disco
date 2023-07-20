# Generated by Django 4.1.9 on 2023-07-20 09:36

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_registered_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmeday',
            name='timeslots',
            field=wagtail.fields.StreamField([('timeslot', wagtail.blocks.StructBlock([('time', wagtail.blocks.CharBlock(required=False)), ('panels_list', wagtail.blocks.StreamBlock([('panel', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('speaker_page', wagtail.blocks.PageChooserBlock(page_type=['home.NewsPage'], required=False)), ('description', wagtail.blocks.TextBlock(required=False))]))], use_json_field=True))]))], blank=True, null=True, use_json_field=True),
        ),
    ]