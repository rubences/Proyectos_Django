# Generated by Django 4.0.7 on 2023-08-03 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_playlist_video'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Playlist',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='videoid',
            new_name='vid_id',
        ),
    ]
