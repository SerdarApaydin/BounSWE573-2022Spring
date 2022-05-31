# Generated by Django 4.0.3 on 2022-05-31 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('space', '0010_space_author_alter_space_spaceimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='space',
            name='spaceImage',
            field=models.ImageField(upload_to='space/images/learningSpaceThumb'),
        ),
    ]