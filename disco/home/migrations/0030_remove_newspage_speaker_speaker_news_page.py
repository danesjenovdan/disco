# Generated by Django 4.1.9 on 2023-08-31 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_remove_organisation_is_participant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspage',
            name='speaker',
        ),
        migrations.AddField(
            model_name='speaker',
            name='news_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.newspage'),
        ),
    ]