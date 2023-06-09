# Generated by Django 4.1.9 on 2023-07-13 17:08

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_newhomepage_exposed_speakers_newspage_speaker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField()),
                ('email', models.URLField()),
                ('country', models.TextField(choices=[('slovenia', 'Slovenia'), ('italy', 'Italy'), ('croatia', 'Croatia')])),
                ('registration_fee', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='programmeday',
            name='timeslots',
            field=wagtail.fields.StreamField([('timeslot', wagtail.blocks.StructBlock([('time', wagtail.blocks.CharBlock()), ('panels_list', wagtail.blocks.StreamBlock([('panel', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('speaker_page', wagtail.blocks.PageChooserBlock(page_type=['home.NewsPage'], required=False)), ('description', wagtail.blocks.TextBlock(required=False))]))], use_json_field=True))]))], use_json_field=True),
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('registered_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.registered')),
                ('applied_for_scholarship', models.BooleanField(default=False)),
                ('previously_supported', models.TextField(blank=True)),
                ('scholarship_motivation', models.TextField(blank=True)),
                ('has_paid', models.BooleanField(default=False)),
                ('scholarship_granted', models.BooleanField(default=False)),
                ('scholarship_denied', models.BooleanField(default=False)),
            ],
            bases=('home.registered',),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('registered_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.registered')),
                ('address', models.TextField()),
                ('vat_id', models.TextField()),
                ('vat_registered', models.BooleanField(default=False)),
                ('has_paid', models.BooleanField(default=False)),
            ],
            bases=('home.registered',),
        ),
        migrations.CreateModel(
            name='IndividualByOrganisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.URLField()),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.organisation')),
            ],
        ),
    ]
