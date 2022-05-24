# Generated by Django 4.0.3 on 2022-05-24 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0007_learningmaterialvideos_video_alter_space_spaceimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('sequence', models.IntegerField()),
                ('video', models.FileField(upload_to='space/materials')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.space')),
            ],
        ),
        migrations.DeleteModel(
            name='LearningMaterialVideos',
        ),
    ]
