from rest_framework import serializers
from .models import *


class Active_Player_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Active_Player_List
        fields = '__all__'

class Sales_TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales_Transactions
        fields = '__all__'

class Actual_Ticket_InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actual_Ticket_Information
        fields = '__all__'

class Winning_TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winning_Tickets
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'