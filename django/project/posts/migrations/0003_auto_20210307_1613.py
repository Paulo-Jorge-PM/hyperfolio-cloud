# Generated by Django 3.1.6 on 2021-03-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210307_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='assets',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.TextField(blank=True, max_length=6000, null=True),
        ),
    ]