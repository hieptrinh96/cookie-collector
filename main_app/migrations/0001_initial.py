# Generated by Django 4.1.3 on 2022-11-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('flavor', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]