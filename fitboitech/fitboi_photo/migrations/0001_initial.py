# Generated by Django 2.2.2 on 2019-11-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommended_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feet', models.FloatField(default=0.0)),
                ('inches', models.FloatField(default=0.0)),
                ('weight', models.FloatField(default=0.0)),
                ('neck', models.FloatField(default=0.0)),
                ('abdomen', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_program', models.CharField(max_length=50)),
                ('recommended_programs', models.ManyToManyField(to='fitboi_photo.Recommended')),
            ],
        ),
    ]
