
from django.contrib import admin
from django.urls import path, include
from lottery import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path(('users/'), include('users.urls')),


    path('active-player-list/', views.Active_Player_ListList, name="active-player-list"),
    path('sales-transactions/', views.Sales_TransactionsList, name="sales-transactions"),
    path('actual-ticket-info/', views.Actual_Ticket_InformationList, name="actual-ticket-info"),
    path('winning-tickets/', views.Winning_TicketsList, name="winning-tickets"),

]
