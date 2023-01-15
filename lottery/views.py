from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from rest_framework.decorators import api_view
from uritemplate import partial
from .serializers import *
from . models import *
from .filters import *

# Create your views here.




@api_view(['GET'])
def Active_Player_ListList(request):
    queryset = Active_Player_List.objects.all()
    filterset = ActivePlayerListFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = Active_Player_ListSerializer(queryset, many=True)
    
    return Response(serializer.data)



@api_view(['GET'])
def Sales_TransactionsList(request):
    queryset = Sales_Transactions.objects.all()
    filterset = SalesTransactionsFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = Sales_TransactionsSerializer(queryset, many=True)
    
    return Response(serializer.data)



@api_view(['GET'])
def Actual_Ticket_InformationList(request):
    queryset = Actual_Ticket_Information.objects.all()
    filterset = ActualTicketInformationFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = Actual_Ticket_InformationSerializer(queryset, many=True)
    
    return Response(serializer.data)



@api_view(['GET'])
def Winning_TicketsList(request):
    queryset = Winning_Tickets.objects.all()
    filterset = WinningTicketsFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = Winning_TicketsSerializer(queryset, many=True)
    
    return Response(serializer.data)