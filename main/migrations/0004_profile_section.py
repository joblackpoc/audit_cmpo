# Generated by Django 4.0.6 on 2022-07-14 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_profile_image_remove_profile_sectionlist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.sectionlist'),
        ),
    ]