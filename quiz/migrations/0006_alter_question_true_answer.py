# Generated by Django 4.0.3 on 2022-05-31 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_question_true_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='true_answer',
            field=models.CharField(blank=True, choices=[(models.CharField(max_length=280, null=True), 'option1'), (models.CharField(max_length=280, null=True), 'option2'), (models.CharField(max_length=280, null=True), 'option3'), (models.CharField(max_length=280, null=True), 'option4')], default=models.CharField(max_length=280, null=True), max_length=280, null=True),
        ),
    ]
