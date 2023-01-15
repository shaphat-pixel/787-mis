from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
User = settings.AUTH_USER_MODEL



class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.phone_number = data.get('phone_number')
        user.name_first = data.get('name_first')
        user.name_last = data.get('name_last')
        user.name_of_company = data.get('name_of_company')

        
        user.save()
        return user