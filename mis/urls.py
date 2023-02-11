
from django.contrib import admin
from django.urls import path, include

from lottery import views
from rest_framework import routers
from django.views.generic import TemplateView


file_router = routers.DefaultRouter()
file_router.register('files', views.FileViewSet, basename='file')

active_player_file_router = routers.DefaultRouter()
active_player_file_router.register('ActivePlayerList', views.ActivePlayerFileViewSet, basename='active-player-file')

actual_ticket_info_router = routers.DefaultRouter()
actual_ticket_info_router.register('ActualTicketInfo', views.ActualTicketInfoFileViewSet, basename = 'actual-ticket-info-file')

sales_transactions_router = routers.DefaultRouter()
sales_transactions_router.register('SalesTransactions', views.SalesTransactionsFileViewSet, basename='sales-transactions-file')


winning_tickets_router = routers.DefaultRouter()
winning_tickets_router.register('WinningTickets', views.WinningTicketsFileViewSet, basename='winning-tickets-file')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),

    path(('users/'), include('users.urls')),


    path('active-player-list/', views.Active_Player_ListList, name="active-player-list"),
    path('sales-transactions/', views.Sales_TransactionsList, name="sales-transactions"),
    path('actual-ticket-info/', views.Actual_Ticket_InformationList, name="actual-ticket-info"),
    path('winning-tickets/', views.Winning_TicketsList, name="winning-tickets"),
    path('mobile-number-directory/', views.Mobile_Number_DirectoryList, name= "mobile-number-directory"),


    path('mobile-number-import/', views.Mobile_Number_Directory_Import, name="mobile-number-import"),
    path('mobile-number-clean/', views.Mobile_Number_Directory_Clean, name="mobile-number-clean"),
    path('file-upload/', include(file_router.urls)),
    path('file-delete/', views.DeleteFile, name="delete file"),


    path('active-player-import/', views.Active_Player_List_Import, name="active-player-list-import"),
    path('active-player-list-clean/', views.Active_Player_List_Clean, name="active-player-list-clean"),
    path('active-player-file-upload/', include(active_player_file_router.urls)),
    path('active-player-file-delete/', views.DeleteActivePlayerFile, name="delete-activer-player-file"),


    path('actual-ticket-info-import/', views.Actual_Ticket_Information_Import, name="actual-ticket-info-import"),
    path('actual-ticket-info-clean/', views.Actual_Ticket_Info_Clean, name="actual-ticket-info-clean"),
    path('actual-ticket-info-file-upload/', include(actual_ticket_info_router.urls)),
    path('actual-ticket-info-file-delete/', views.DeleteActualTicketInfoFile, name="delete-actual-player-info-file"),


    path('sales-transactions-import/', views.Sales_Transactions_List_Import, name="sales-transactions-import"),
    path('sales-transactions-clean/', views.Sales_Transactions_Clean, name="sales-transactions-clean"),
    path('sales-transactions-file-upload/', include(sales_transactions_router.urls)),
    path('sales-transactions-file-delete/', views.DeleteSalesTransactionsFile, name="delete-sales-transactions-file"),

    path('winning-tickets-import/', views.Winning_Tickets_Import, name="winning-tickets-import"),
    path('winning-tickets-clean/', views.Winning_Tickets_Clean, name="winning-tickets-clean"),
    path('winning-tickets-file-upload/', include(winning_tickets_router.urls)),
    path('winning-tickets-file-delete/', views.DeleteWinningTicketsFile, name="delete-winning-rickets-file"),

]
