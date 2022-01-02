from django.shortcuts import render
from rest_framework import generics, permissions
from .serializer import AddSerializer,MyTokenObtainPairSerializer,EditSerializer
from .models import Account
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView



# Create your views here.

class CustomObtainAuthToken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class AddListView(generics.CreateAPIView):
    serializer_class = AddSerializer
    queryset = Account.objects.all()
    permission_classes = [permissions.AllowAny]

class DetailAddView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EditSerializer
    queryset = Account.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get_object(self):
        UserName= self.kwargs.get("username")
        return get_object_or_404(Account, username=UserName)
class ListView(generics.ListAPIView):
    serializer_class = AddSerializer
    queryset = Account.objects.all()
    permission_classes = [permissions.AllowAny]