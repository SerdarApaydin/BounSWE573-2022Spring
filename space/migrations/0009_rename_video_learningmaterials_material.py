# Generated by Django 4.0.3 on 2022-05-24 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0008_learningmaterials_delete_learningmaterialvideos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learningmaterials',
            old_name='video',
            new_name='material',
        ),
    ]
