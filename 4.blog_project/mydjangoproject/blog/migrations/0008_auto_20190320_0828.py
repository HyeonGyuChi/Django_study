# Generated by Django 2.1.5 on 2019-03-20 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190320_0827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['pub_date']},
        ),
    ]