# Generated by Django 3.2.7 on 2022-08-31 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_staff_linkedin_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(upload_to='personimages'),
        ),
    ]
