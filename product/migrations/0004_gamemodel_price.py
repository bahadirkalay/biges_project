# Generated by Django 3.1.1 on 2021-02-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_gamemodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemodel',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]