# Generated by Django 4.0.2 on 2022-02-21 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fly', '0006_delete_searchflights'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmbooking',
            name='journey_date',
            field=models.DateField(auto_now=True),
        ),
    ]