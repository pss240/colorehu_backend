# Generated by Django 4.2.1 on 2023-06-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colorset', '0003_alter_colorset_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorset',
            name='color2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='colorset',
            name='color3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='colorset',
            name='color4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='colorset',
            name='color5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
