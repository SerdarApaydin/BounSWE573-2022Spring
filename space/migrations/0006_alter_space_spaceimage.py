# Generated by Django 4.0.3 on 2022-05-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0005_alter_space_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='spaceImage',
            field=models.ImageField(upload_to='space/LearningSpaceImages'),
        ),
    ]
