# Generated by Django 4.2.3 on 2023-07-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_callhistory_call_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callhistory',
            name='Call_time',
        ),
        migrations.AddField(
            model_name='callhistory',
            name='fx',
            field=models.FloatField(null=True),
        ),
    ]
