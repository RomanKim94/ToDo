# Generated by Django 3.1.14 on 2023-12-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]