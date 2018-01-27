from .models import Travel
from rest_framework import serializers
from django.contrib.auth.models import User
#from snippets.models import Snippet

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel 
        fields = ('id', 'destination', 'start_date', 'end_date', 'user_id')


class UserSerializer(serializers.ModelSerializer):
    #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username')
