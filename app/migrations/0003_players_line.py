# Generated by Django 3.0.6 on 2020-05-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200526_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='line',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
