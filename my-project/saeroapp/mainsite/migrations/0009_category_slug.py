# Generated by Django 3.2.7 on 2022-09-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_alter_staff_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]