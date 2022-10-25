# Generated by Django 3.2.7 on 2022-10-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0016_auto_20221017_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='galleryimages')),
                ('explanation', models.CharField(max_length=250)),
                ('date', models.DateField()),
            ],
        ),
    ]
