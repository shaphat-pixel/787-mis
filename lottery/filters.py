from . models import *
import django_filters

class ActivePlayerListFilter(django_filters.FilterSet):
    class Meta:
        model = Active_Player_List
        fields = ['player_name', 'mobile_number', 'promo_request']


class SalesTransactionsFilter(django_filters.FilterSet):
    class Meta:
        model = Sales_Transactions
        fields = ['player_name', 'mobile_number', 'network', 'number_of_tickets', 'amount']

class ActualTicketInformationFilter(django_filters.FilterSet):
    class Meta:
        model = Actual_Ticket_Information
        fields = ['player_name', 'mobile_number', 'price']


class WinningTicketsFilter(django_filters.FilterSet):
    class Meta:
        model = Winning_Tickets
        fields = ['player_name', 'mobile_number', 'draw_id', 'ticket_number', 'price_amount', 'price_category']