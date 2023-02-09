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
from sqlalchemy import create_engine
import psycopg2 
import io
import pandas as pd

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, permissions
import shutil
import os
from mis.settings import BASE_DIR


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
def Active_Player_List_Import(request):


     engine = create_engine(
     'postgresql+psycopg2://linpostgres:ySDTo2EbCoRw+3XG@lin-16005-5195-pgsql-primary.servers.linodedb.net:5432/postgres')


     df = pd.read_csv('ActivePlayerList/*.csv')
     # Drop old table and create new empty table
     df.head(0).to_sql('active_player_list', engine, if_exists='append',index=False)

     conn = engine.raw_connection()
     cur = conn.cursor()
     output = io.StringIO()
     df.to_csv(output, sep='\t', header=False, index=False)
     output.seek(0)
     contents = output.getvalue()
     cur.copy_from(output, 'active_player_list', null="") # null values become ''
     conn.commit()
     cur.close()
     conn.close()
     
     return Response("Active Players listed successfully") 

"""
@api_view(['GET'])
def Active_Player_List_Clean(request):
     lastSeenId = float('-Inf')
     rows = Mobile_Number_Directory.objects.all().order_by('mobile_number')

     for row in rows:
          if row.mobile_number == lastSeenId:
               row.delete() # We've seen this id in a previous row
          else: # New id found, save it and check future rows for duplicates.
               lastSeenId = row.mobile_number
     return Response("Duplicates eliminated successfully")
"""

class ActivePlayerFileViewSet(viewsets.ModelViewSet):
     queryset = Active_Player_File.objects.all()
     serializer_class = ActivePlayerSerializer
     permission_classes = [permissions.AllowAny]

@api_view(['GET'])
def DeleteActivePlayerFile(request):
          # This is your folder path
     file_location = os.path.join(BASE_DIR, 'ActivePlayerList')

     # Here, lets delete the file
     shutil.rmtree(file_location, ignore_errors = True)
     # making ignore_errors = True will not raise a FileNotFoundError
     return Response("file deleted successfully!")




@api_view(['GET'])
def Sales_TransactionsList(request):
    queryset = Sales_Transactions.objects.all()
    filterset = SalesTransactionsFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = Sales_TransactionsSerializer(queryset, many=True)
    
    return Response(serializer.data)



@api_view(['GET'])
def Sales_Transactions_List_Import(request):


     engine = create_engine(
     'postgresql+psycopg2://linpostgres:ySDTo2EbCoRw+3XG@lin-16005-5195-pgsql-primary.servers.linodedb.net:5432/postgres')


     df = pd.read_csv('SalesTransactions/*.csv')
     # Drop old table and create new empty table
     df.head(0).to_sql('sales_transactions', engine, if_exists='append',index=False)

     conn = engine.raw_connection()
     cur = conn.cursor()
     output = io.StringIO()
     df.to_csv(output, sep='\t', header=False, index=False)
     output.seek(0)
     contents = output.getvalue()
     cur.copy_from(output, 'sales_transactions', null="") # null values become ''
     conn.commit()
     cur.close()
     conn.close()
     
     return Response("Sales Transactions listed successfully") 

"""
@api_view(['GET'])
def Active_Player_List_Clean(request):
     lastSeenId = float('-Inf')
     rows = Mobile_Number_Directory.objects.all().order_by('mobile_number')

     for row in rows:
          if row.mobile_number == lastSeenId:
               row.delete() # We've seen this id in a previous row
          else: # New id found, save it and check future rows for duplicates.
               lastSeenId = row.mobile_number
     return Response("Duplicates eliminated successfully")
"""

class SalesTransactionsFileViewSet(viewsets.ModelViewSet):
     queryset = Sales_Transactions_File.objects.all()
     serializer_class = SalesTransactionsSerializer
     permission_classes = [permissions.AllowAny]

@api_view(['GET'])
def DeleteSalesTransactionsFile(request):
          # This is your folder path
     file_location = os.path.join(BASE_DIR, 'SalesTransactions')

     # Here, lets delete the file
     shutil.rmtree(file_location, ignore_errors = True)
     # making ignore_errors = True will not raise a FileNotFoundError
     return Response("file deleted successfully!")




@api_view(['GET'])
def Actual_Ticket_InformationList(request):
    queryset = Actual_Ticket_Information.objects.all()
    filterset = ActualTicketInformationFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = Actual_Ticket_InformationSerializer(queryset, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def Actual_Ticket_Information_Import(request):


     engine = create_engine(
     'postgresql+psycopg2://linpostgres:ySDTo2EbCoRw+3XG@lin-16005-5195-pgsql-primary.servers.linodedb.net:5432/postgres')


     df = pd.read_csv('ActualTicketInfo/*.csv')
     # Drop old table and create new empty table
     df.head(0).to_sql('actual_ticket_info', engine, if_exists='append',index=False)

     conn = engine.raw_connection()
     cur = conn.cursor()
     output = io.StringIO()
     df.to_csv(output, sep='\t', header=False, index=False)
     output.seek(0)
     contents = output.getvalue()
     cur.copy_from(output, 'actual_ticket_info', null="") # null values become ''
     conn.commit()
     cur.close()
     conn.close()
     
     return Response("Actual Ticket Info Listed ") 

"""
@api_view(['GET'])
def Active_Player_List_Clean(request):
     lastSeenId = float('-Inf')
     rows = Mobile_Number_Directory.objects.all().order_by('mobile_number')

     for row in rows:
          if row.mobile_number == lastSeenId:
               row.delete() # We've seen this id in a previous row
          else: # New id found, save it and check future rows for duplicates.
               lastSeenId = row.mobile_number
     return Response("Duplicates eliminated successfully")
"""

class ActualTicketInfoFileViewSet(viewsets.ModelViewSet):
     queryset = Actual_Ticket_Info_File.objects.all()
     serializer_class = ActualTicketInfoSerializer
     permission_classes = [permissions.AllowAny]

@api_view(['GET'])
def DeleteActualTicketInfoFile(request):
          # This is your folder path
     file_location = os.path.join(BASE_DIR, 'ActualTicketInfo')

     # Here, lets delete the file
     shutil.rmtree(file_location, ignore_errors = True)
     # making ignore_errors = True will not raise a FileNotFoundError
     return Response("file deleted successfully!")




@api_view(['GET'])
def Winning_TicketsList(request):
    queryset = Winning_Tickets.objects.all()
    filterset = WinningTicketsFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = Winning_TicketsSerializer(queryset, many=True)
    
    return Response(serializer.data)




@api_view(['GET'])
def Winning_Tickets_Import(request):


     engine = create_engine(
     'postgresql+psycopg2://linpostgres:ySDTo2EbCoRw+3XG@lin-16005-5195-pgsql-primary.servers.linodedb.net:5432/postgres')


     df = pd.read_csv('WinningTickets/*.csv')
     # Drop old table and create new empty table
     df.head(0).to_sql('winning_tickets', engine, if_exists='append',index=False)

     conn = engine.raw_connection()
     cur = conn.cursor()
     output = io.StringIO()
     df.to_csv(output, sep='\t', header=False, index=False)
     output.seek(0)
     contents = output.getvalue()
     cur.copy_from(output, 'winning_tickets', null="") # null values become ''
     conn.commit()
     cur.close()
     conn.close()
     
     return Response("Winning Tickets Listed successfully ") 

"""
@api_view(['GET'])
def Active_Player_List_Clean(request):
     lastSeenId = float('-Inf')
     rows = Mobile_Number_Directory.objects.all().order_by('mobile_number')

     for row in rows:
          if row.mobile_number == lastSeenId:
               row.delete() # We've seen this id in a previous row
          else: # New id found, save it and check future rows for duplicates.
               lastSeenId = row.mobile_number
     return Response("Duplicates eliminated successfully")
"""

class WinningTicketsFileViewSet(viewsets.ModelViewSet):
     queryset = Winning_Tickets_File.objects.all()
     serializer_class = WinningTicketsSerializer
     permission_classes = [permissions.AllowAny]

@api_view(['GET'])
def DeleteWinningTicketsFile(request):
          # This is your folder path
     file_location = os.path.join(BASE_DIR, 'WinningTickets')

     # Here, lets delete the file
     shutil.rmtree(file_location, ignore_errors = True)
     # making ignore_errors = True will not raise a FileNotFoundError
     return Response("file deleted successfully!")



@api_view(['GET'])
def Mobile_Number_DirectoryList(request):
    queryset = Mobile_Number_Directory.objects.all()
    filterset = MobileNumberDirectoryFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = Mobile_Number_DirectorySerializer(queryset, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def Mobile_Number_Directory_Import(request):


     engine = create_engine(
     'postgresql+psycopg2://linpostgres:ySDTo2EbCoRw+3XG@lin-16005-5195-pgsql-primary.servers.linodedb.net:5432/postgres')


     df = pd.read_csv('./files/*.csv')
     # Drop old table and create new empty table
     df.head(0).to_sql('mobile_number_directory', engine, if_exists='append',index=False)

     conn = engine.raw_connection()
     cur = conn.cursor()
     output = io.StringIO()
     df.to_csv(output, sep='\t', header=False, index=False)
     output.seek(0)
     contents = output.getvalue()
     cur.copy_from(output, 'mobile_number_directory', null="") # null values become ''
     conn.commit()
     cur.close()
     conn.close()
     
     return Response("Mobile numbers imported successfully ") 


@api_view(['GET'])
def Mobile_Number_Directory_Clean(request):
     lastSeenId = float('-Inf')
     rows = Mobile_Number_Directory.objects.all().order_by('mobile_number')

     for row in rows:
          if row.mobile_number == lastSeenId:
               row.delete() # We've seen this id in a previous row
          else: # New id found, save it and check future rows for duplicates.
               lastSeenId = row.mobile_number
     return Response("Duplicates eliminated successfully")

class FileViewSet(viewsets.ModelViewSet):
     queryset = File.objects.all()
     serializer_class = FileSerializer
     permission_classes = [permissions.AllowAny]

@api_view(['GET'])
def DeleteFile(request):
          # This is your folder path
     file_location = os.path.join(BASE_DIR, 'files')

     # Here, lets delete the file
     shutil.rmtree(file_location, ignore_errors = True)
     # making ignore_errors = True will not raise a FileNotFoundError
     return Response("file deleted successfully!")
            
                 
