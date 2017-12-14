from .models import Web
from rest_framework import serializers

class webSerializer(serializers.ModelSerializer):

    class Meta:
        model = Web
        fields = '__all__'
        #fileds = ('id', 'name', 'open')