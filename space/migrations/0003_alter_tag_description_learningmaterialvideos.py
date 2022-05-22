# Generated by Django 4.0.3 on 2022-05-21 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(max_length=32),
        ),
        migrations.CreateModel(
            name='LearningMaterialVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('seq_number', models.IntegerField()),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.space')),
            ],
        ),
    ]
