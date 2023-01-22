from . models import Mobile_Number_Directory


for row in Mobile_Number_Directory.objects.all().reverse():
    if Mobile_Number_Directory.objects.filter(mobile_number=row.mobile_number).count() > 1:
        row.delete()