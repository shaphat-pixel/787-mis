# Generated by Django 4.0 on 2023-01-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile_Number_Directory',
            fields=[
                ('mobile_number', models.IntegerField(primary_key=True, serialize=False)),
                ('source', models.CharField(default='', max_length=200)),
            ],
        ),
    ]