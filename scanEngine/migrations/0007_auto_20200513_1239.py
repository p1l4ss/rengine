# Generated by Django 3.0.6 on 2020-05-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0006_auto_20200513_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enginetype',
            name='subdomain_discovery',
            field=models.BooleanField(default=True),
        ),
    ]