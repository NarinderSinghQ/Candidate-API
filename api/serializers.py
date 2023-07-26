from rest_framework import serializers
from .models import *

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class CallHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Callhistory
        fields = '__all__'
        
    # Candidate_Name = serializers.SerializerMethodField()

    # def get_Candidate_Name(self, obj):
    #     return obj.Candidate.Name
