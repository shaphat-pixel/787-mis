
from django.contrib import admin
from django.urls import path, include

from lottery import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('files', views.FileViewSet, basename='file')

urlpatterns = [
    path('admin/', admin.site.urls),

    path(('users/'), include('users.urls')),


    path('active-player-list/', views.Active_Player_ListList, name="active-player-list"),
    path('sales-transactions/', views.Sales_TransactionsList, name="sales-transactions"),
    path('actual-ticket-info/', views.Actual_Ticket_InformationList, name="actual-ticket-info"),
    path('winning-tickets/', views.Winning_TicketsList, name="winning-tickets"),
    path('mobile-number-import/', views.Mobile_Number_Directory_Import, name="mobile-number-import"),
    path('mobile-number-clean/', views.Mobile_Number_Directory_Clean, name="mobile-number-clean"),
    path('file-upload/', include(router.urls)),
    path('file-delete/', views.DeleteFile, name="delete file"),

]
