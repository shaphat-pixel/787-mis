from import_export import resources
from import_export.instance_loaders import CachedInstanceLoader
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




class Mobile_Number_Directory_Resource(resources.ModelResource):
    
    class Meta:
        model = Mobile_Number_Directory
        skip_unchanged = True
        skip_diff = True
        use_bulk=True
        batch_size = None
        instance_loader_class = CachedInstanceLoader





