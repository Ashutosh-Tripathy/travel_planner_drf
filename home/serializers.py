from .models import Travel
from rest_framework import serializers


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel 
        fields = ('destination', 'start_date', 'end_date', 'user_id')
