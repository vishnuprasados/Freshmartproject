# Generated by Django 4.2.6 on 2024-03-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0005_placeorder_mobile_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeorder',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
