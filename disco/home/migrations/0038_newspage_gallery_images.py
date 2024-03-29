# Generated by Django 4.1.9 on 2023-11-02 10:15

from django.db import migrations
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_newhomepage_stream_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='gallery_images',
            field=wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, use_json_field=True),
        ),
    ]
