# Generated by Django 4.2.5 on 2023-09-17 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
            ],
        ),
    ]
