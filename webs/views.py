from django.shortcuts import render, get_object_or_404
from .serializers import webSerializer
from rest_framework import status
# from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .models import Web
from rest_framework.response import Response
from django.http import Http404

class WebApi(APIView):

    def get_objects(self, pk):
        try:
            return Web.objects.get(pk=pk)
        except Web.DoesNotExist:
            return Http404

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
    def delete(self, request, pk):
        Web.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)