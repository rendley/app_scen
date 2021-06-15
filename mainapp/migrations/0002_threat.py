# Generated by Django 3.2 on 2021-05-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Угроза безопасности')),
                ('number', models.PositiveIntegerField(verbose_name='Идентификатор тактики')),
            ],
        ),
    ]