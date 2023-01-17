from import_export import resources
from . models import *

class Active_Player_ListResource(resources.ModelResource):
    class Meta:
        model = Active_Player_List

class Sales_TransactionsResource(resources.ModelResource):
    class Meta:
        model = Sales_Transactions

class Actual_Ticket_InformationResource(resources.ModelResource):
    class Meta:
        model = Actual_Ticket_Information

class Winning_TicketsResource(resources.ModelResource):
    class Meta:
        model = Winning_Tickets

class Mobile_Number_Directory(resources.ModelResource):
    class Meta:
        model = Mobile_Number_Directory

    def skip_row(self, instance, original):
        #return True if Mobile_Number_Directory.objects.filter(mobile_number=instance.mobile_number).exists() else False
        if Mobile_Number_Directory.objects.filter(mobile_number=instance.mobile_number).exists():
            return True
        else:
            return False



