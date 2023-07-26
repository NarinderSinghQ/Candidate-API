from rest_framework import serializers
from .models import *


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"


class CallHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Callhistory
        # exclude = ("Candidate",)
        fields = '__all__'
        extra_kwargs = {
            'candidate': {'required': False}
        }

    # Candidate_Name = serializers.SerializerMethodField()

    # def get_Candidate_Name(self, obj):
    #     return obj.Candidate.Name
