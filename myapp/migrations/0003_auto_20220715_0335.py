# Generated by Django 3.2 on 2022-07-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rule',
            old_name='name',
            new_name='docsdiv',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='rule',
        ),
        migrations.AddField(
            model_name='rule',
            name='specs',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rule',
            name='wbs1',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rule',
            name='wbs2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rule',
            name='wbs3',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rule',
            name='wbs_code',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
