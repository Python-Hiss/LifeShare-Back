from django.db.models import fields
from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AddSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = Account.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            age=validated_data['age'],
            group = validated_data['group'],
            blood_type = validated_data['blood_type'],
            chronic_diseases = validated_data['chronic_diseases'],
            data = validated_data['data'],
            phone_number = validated_data['phone_number'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            location = validated_data['location'],
            donate = validated_data['donate'],
            image = validated_data['image']
        )

        return user

    class Meta:
        model = Account
        fields = ('id','first_name','last_name','username',
        'email','password','age','blood_type','phone_number','location',
        'chronic_diseases','data','donate','group','image'
        )

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['id'] = self.user.id
        data['username'] = self.user.username

        return data

