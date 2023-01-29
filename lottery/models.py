from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Active_Player_List(models.Model):
    player_id = models.CharField(default="", max_length=100)
    last_name = models.CharField(default="", max_length=100)
    other_name = models.CharField(default="", max_length=100)
    mobile_number = models.CharField(default="", max_length=100)
    promo_request = models.CharField(default="", max_length=100)
    date_created = models.CharField(default="", max_length=100)


    class Meta:
        db_table = 'active_player_list'
        managed = False


    def __str__(self):
        return f'{self.player_name}'
    


class Sales_Transactions(models.Model):
    transaction_date = models.CharField(default="", max_length=100)
    transaction_id = models.CharField(default="", max_length=100)
    mobile_number =  models.CharField(default="", max_length=100)
    player_name = models.CharField(default="", max_length=100)
    network = models.CharField(default="", max_length=100)
    number_of_tickets = models.PositiveIntegerField()
    amount = models.IntegerField()

    class Meta:
        db_table = 'sales_transactions'
        managed = False


    def __str__(self):
        return f'{self.player_name}'
    

class Actual_Ticket_Information(models.Model):
    player_name = models.CharField(default="", max_length=100)
    mobile_number = models.CharField(default="", max_length=100)
    price=models.CharField(max_length=300, default="")
    date_created=models.CharField(max_length=100, default="")

    class Meta:
        db_table = 'actual_ticket_info'
        managed = False
    

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
    mobile_number = models.CharField(primary_key=True, validators=[MinLengthValidator(12)], max_length=12)
    source = models.CharField(default="", max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'mobile_number_directory'
        managed = False

    def __str__(self):
        return f'{self.mobile_number}'


class File(models.Model):
    file = models.FileField(upload_to="files")


class Active_Player_File(models.Model):
    file = models.FileField(upload_to="ActivePlayerList")


class Actual_Ticket_Info_File(models.Model):
    file = models.FileField(upload_to="ActualTicketInfo")

class Sales_Transactions_File(models.Model):
    file = models.FileField(upload_to="SalesTransactions")


class Winning_Tickets_File(models.Model):
    file = models.FileField(upload_to="WinningTickets")

