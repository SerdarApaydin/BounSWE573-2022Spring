# Generated by Django 4.0.3 on 2022-05-31 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0012_alter_space_spaceimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='spaceImage',
            field=models.ImageField(upload_to='space/images/learningSpaceThumb'),
        ),
    ]
