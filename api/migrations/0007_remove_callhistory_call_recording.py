# Generated by Django 4.2.3 on 2023-07-25 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_callhistory_call_recording'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callhistory',
            name='call_recording',
        ),
    ]
