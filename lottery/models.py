from django.db import models

from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Active_Player_List(models.Model):
    player_name = models.CharField(default="", max_length=100)
    mobile_number = models.CharField(default="", max_length=100)
    promo_request = models.BooleanField(default=False)
    date_created = models.CharField(default="", max_length=100)


    def __str__(self):
        return f'{self.player_name}'
    


class Sales_Transactions(models.Model):
    player_name = models.CharField(default="", max_length=100)
    mobile_number = models.CharField(default="", max_length=100)
    network = models.CharField(default="", max_length=100)
    number_of_tickets = models.PositiveIntegerField()
    amount = models.IntegerField()


    def __str__(self):
        return f'{self.player_name}'
    

class Actual_Ticket_Information(models.Model):
    player_name = models.CharField(default="", max_length=100)
    mobile_number = models.CharField(default="", max_length=100)
    price=models.CharField(max_length=300, default="")
    date_created=models.CharField(max_length=100, default="")
    

    def __str__(self):
        return f'{self.player_name}'
    

class Winning_Tickets(models.Model):
    draw_id = models.IntegerField()
    draw_name = models.IntegerField()
    player_name = models.CharField(default="", max_length=100)
    mobile_number = models.CharField(default="", max_length=100)
    ticket_number = models.CharField(default="", max_length=100)
    price_amount=models.CharField(max_length=100, default="")
    price_category=models.CharField(max_length=100, default="")

    def __str__(self):
        return f'{self.player_name}'


class Mobile_Number_Directory(models.Model):
    mobile_number = models.IntegerField()
    source = models.CharField(default="", max_length=200)

    def __str__(self):
        return f'{self.mobile_number}'