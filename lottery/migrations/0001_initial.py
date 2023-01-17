# Generated by Django 4.0 on 2023-01-17 23:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Active_Player_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('other_name', models.CharField(default='', max_length=100)),
                ('mobile_number', models.CharField(default='', max_length=100)),
                ('promo_request', models.BooleanField(default=False)),
                ('date_created', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Actual_Ticket_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(default='', max_length=100)),
                ('mobile_number', models.CharField(default='', max_length=100)),
                ('price', models.CharField(default='', max_length=300)),
                ('date_created', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile_Number_Directory',
            fields=[
                ('id', models.CharField(default='', max_length=100)),
                ('mobile_number', models.CharField(max_length=12, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(12)])),
                ('source', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sales_Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.CharField(default='', max_length=100)),
                ('transaction_id', models.CharField(default='', max_length=100)),
                ('mobile_number', models.CharField(default='', max_length=100)),
                ('player_name', models.CharField(default='', max_length=100)),
                ('network', models.CharField(default='', max_length=100)),
                ('number_of_tickets', models.PositiveIntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Winning_Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_id', models.IntegerField()),
                ('draw_name', models.IntegerField()),
                ('player_name', models.CharField(default='', max_length=100)),
                ('mobile_number', models.CharField(default='', max_length=100)),
                ('ticket_number', models.CharField(default='', max_length=100)),
                ('price_amount', models.CharField(default='', max_length=100)),
                ('price_category', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
