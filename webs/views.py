from .serializers import webSerializer
from .models import Web
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from rest_framework import generics
from rest_framework.permissions import (
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        AllowAny,
        IsAdminUser
)
import django_filters.rest_framework

class WebApi(generics.ListCreateAPIView):
    queryset = Web.objects.all()
    serializer_class = webSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class WebApiDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Web.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = webSerializer

class UserListView(generics.ListAPIView):
    queryset = Web.objects.all()
    serializer_class = webSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/web/')
            else:
                messages.error(request, 'Username or password did not match')
        except ObjectDoesNotExist:
            print("Invalide user")
    return render(request, 'webs/login.html')
