from email.policy import default
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from . models import *

from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.serializers import PasswordResetSerializer
from django.conf import settings

from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=100)
    name_first = serializers.CharField(max_length=100)
    name_last = serializers.CharField(max_length=100)
    name_of_company = serializers.CharField(max_length=100)
    

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['phone_number'] = self.validated_data.get('phone_number', '')
        data_dict['name_first'] = self.validated_data.get('name_first', '')
        data_dict['name_last'] = self.validated_data.get('name_last', '')
        data_dict['name_of_company'] = self.validated_data.get('name_of_company', '')

        return data_dict


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
            ('phone_number', 'name_first', 'name_last', 'name_of_company')



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

