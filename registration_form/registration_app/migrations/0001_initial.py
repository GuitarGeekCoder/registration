# Generated by Django 5.0 on 2023-12-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('course', models.CharField(choices=[('Mca', 'Mca'), ('B.E/B.tech', 'B.E/B.tech'), ('Bca', 'Bca'), ('Polytechnic', 'Polytechnic'), ('ITI', 'ITI')], max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=255)),
                ('department', models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EC', 'EC')], max_length=255)),
                ('college_name', models.CharField(max_length=255)),
            ],
        ),
    ]