# Generated by Django 3.0.2 on 2020-02-01 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='password',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='username',
        ),
        migrations.AddField(
            model_name='venue',
            name='img',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
