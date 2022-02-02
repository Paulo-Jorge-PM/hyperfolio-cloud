# Generated by Django 3.1.6 on 2021-03-07 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='privacy',
            field=models.CharField(choices=[('Public', 'Public'), ('Friends', 'Friends'), ('Me', 'Me')], default='Public', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withPersons', models.TextField(blank=True, max_length=500)),
                ('postId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.TextField(blank=True, max_length=1000)),
                ('organizations', models.TextField(blank=True, max_length=1000)),
                ('withPersons', models.TextField(blank=True, max_length=500)),
                ('postId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateStart', models.DateField(null=True)),
                ('dateEnd', models.DateField(blank=True, null=True)),
                ('categories', models.TextField(blank=True, max_length=1000)),
                ('organizations', models.TextField(blank=True, max_length=500)),
                ('locations', models.TextField(blank=True, max_length=500)),
                ('withPersons', models.TextField(blank=True, max_length=500)),
                ('postId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]