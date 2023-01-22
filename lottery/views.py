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
from pangres import upsert
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
     lastSeenId = float('-Inf')
     rows = Mobile_Number_Directory.objects.all().order_by('mobile_number')

     for row in rows:
          if row.mobile_number == lastSeenId:
               row.delete() # We've seen this id in a previous row
          else: # New id found, save it and check future rows for duplicates.
               lastSeenId = row.mobile_number
     return Response("Duplicates eliminated successfully") 


@api_view(['GET'])
def Mobile_Number_Directory_Import(request):


     engine = create_engine(
     'postgresql+psycopg2://linpostgres:^ycZUaSzWOrsK37E@lin-15054-4726-pgsql-primary.servers.linodedb.net:5432/postgres')


     df = pd.read_csv('files/data.csv')
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
            
                 
