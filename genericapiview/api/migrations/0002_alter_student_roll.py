# Generated by Django 4.2.8 on 2024-01-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.CharField(max_length=50),
        ),
    ]