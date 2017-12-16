from django.shortcuts import render, get_object_or_404
from .serializers import webSerializer
# from rest_framework import status
# from rest_framework.status import HTTP_400_BAD_REQUEST
# from rest_framework.views import APIView
from .models import Web
# from rest_framework.response import Response
# from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import (
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        AllowAny,
        IsAdminUser
)

'''class WebApi(APIView):

    def get(self, request):
        webs = Web.objects.all()
        serializer = webSerializer(webs, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = webSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebApiDetails(APIView):
    def get_objects(self, pk):
        try:
            return  Web.objects.get(pk=pk)
        except Web.DoesNotExist:
            return Http404

    def get(self, request, pk):
        web = self.get_objects(pk)
        serializer = webSerializer(web)
        return Response(serializer.data)

    def put(self, request, pk):
        web = self.get_objects(pk)
        serializer = webSerializer(web, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        web = self.get_objects(pk)
        web.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''

class WebApi(generics.ListCreateAPIView):
    queryset = Web.objects.all()
    serializer_class = webSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class WebApiDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Web.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = webSerializer