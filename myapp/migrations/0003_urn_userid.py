# Generated by Django 3.2 on 2022-06-02 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_model_urn'),
    ]

    operations = [
        migrations.AddField(
            model_name='urn',
            name='userId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
