# Generated by Django 4.2.6 on 2023-12-06 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='pass', max_length=50),
        ),
    ]
