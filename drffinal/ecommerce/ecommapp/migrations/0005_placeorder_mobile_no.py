# Generated by Django 4.2.6 on 2024-03-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0004_placeorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeorder',
            name='mobile_no',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
