# Generated by Django 4.0.3 on 2022-05-20 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=280, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('spaceImage', models.ImageField(upload_to='LearningSpaceImages')),
            ],
        ),
    ]
