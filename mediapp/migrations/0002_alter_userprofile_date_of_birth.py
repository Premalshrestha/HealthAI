# Generated by Django 5.2.4 on 2025-07-30 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
