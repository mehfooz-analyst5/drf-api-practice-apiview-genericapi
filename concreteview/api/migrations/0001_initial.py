# Generated by Django 4.2.8 on 2024-01-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('roll', models.IntegerField()),
                ('department', models.CharField(max_length=255)),
                ('semester', models.IntegerField()),
                ('university', models.CharField(max_length=255)),
                ('campus', models.CharField(max_length=255)),
            ],
        ),
    ]
