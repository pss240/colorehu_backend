# Generated by Django 4.2.1 on 2023-06-03 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color1', models.CharField(max_length=200)),
                ('color2', models.CharField(blank=True, max_length=200)),
                ('color3', models.CharField(blank=True, max_length=200)),
                ('color4', models.CharField(blank=True, max_length=200)),
                ('color5', models.CharField(blank=True, max_length=200)),
                ('share', models.BooleanField(default=False)),
                ('keyword', models.CharField(max_length=200)),
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to='signin.signin')),
            ],
        ),
    ]
