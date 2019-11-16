# Generated by Django 2.2.7 on 2019-11-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitboi_photo', '0003_auto_20191116_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommended_Programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_program', models.CharField(max_length=50)),
                ('Recommended_Programs', models.ManyToManyField(to='fitboi_photo.Recommended_Programs')),
            ],
        ),
    ]
