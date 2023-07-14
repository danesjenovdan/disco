# Generated by Django 4.1.9 on 2023-07-14 18:22

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_newhomepage_exposed_speakers_speaker_exposed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmeday',
            name='timeslots',
            field=wagtail.fields.StreamField([('timeslot', wagtail.blocks.StructBlock([('time', wagtail.blocks.CharBlock(required=False)), ('panels_list', wagtail.blocks.StreamBlock([('panel', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('speaker_page', wagtail.blocks.PageChooserBlock(page_type=['home.NewsPage'], required=False)), ('description', wagtail.blocks.TextBlock(required=False))]))], use_json_field=True))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='social_media',
            field=wagtail.fields.StreamField([('instagram', wagtail.blocks.URLBlock()), ('mastodon', wagtail.blocks.URLBlock()), ('twitter', wagtail.blocks.URLBlock()), ('facebook', wagtail.blocks.URLBlock()), ('website', wagtail.blocks.URLBlock()), ('podcast', wagtail.blocks.URLBlock()), ('linkedin', wagtail.blocks.URLBlock()), ('youtube', wagtail.blocks.URLBlock()), ('tiktok', wagtail.blocks.URLBlock())], blank=True, use_json_field=True),
        ),
    ]
