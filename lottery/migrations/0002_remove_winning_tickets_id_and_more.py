# Generated by Django 4.0 on 2023-02-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='winning_tickets',
            name='id',
        ),
        migrations.AlterField(
            model_name='winning_tickets',
            name='draw_id',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
