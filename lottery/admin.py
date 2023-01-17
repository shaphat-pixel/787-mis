from django.contrib import admin

from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Active_Player_List)
class Active_Player_ListAdmin(ImportExportModelAdmin):
    list_display = ("player_id", "last_name", "other_name", "mobile_number", "promo_request", "date_created")
    pass


@admin.register(Sales_Transactions)
class SalesTransactionsAdmin(ImportExportModelAdmin):
    list_display = ("transaction_date", "transaction_id", "player_name", "mobile_number", "network", "number_of_tickets", "amount")
    pass


@admin.register(Actual_Ticket_Information)
class Actual_Ticket_InformationAdmin(ImportExportModelAdmin):
    list_display = ("player_name", "mobile_number", "price", "date_created")
    pass


@admin.register(Winning_Tickets)
class Winning_TicketsAdmin(ImportExportModelAdmin):
    list_display = ("draw_id", "draw_name", "player_name", "mobile_number", "ticket_number", "price_amount", "price_category")
    pass


@admin.register(Mobile_Number_Directory)
class Mobile_Number_Directory(ImportExportModelAdmin):
    list_display = ("mobile_number", "source")
    pass

