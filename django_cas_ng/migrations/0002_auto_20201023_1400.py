# Generated by Django 2.2.16 on 2020-10-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_cas_ng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxygrantingticket',
            name='session_key',
            field=models.CharField(blank=True, max_length=736, null=True),
        ),
        migrations.AlterField(
            model_name='sessionticket',
            name='session_key',
            field=models.CharField(max_length=736),
        ),
    ]
