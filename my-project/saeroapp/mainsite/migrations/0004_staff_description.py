# Generated by Django 3.2.7 on 2022-08-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_alter_staff_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='description',
            field=models.TextField(null=True),
        ),
    ]