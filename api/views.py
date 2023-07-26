from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters
from .pagination import *


class CandidateListView(generics.ListCreateAPIView):
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    ordering_fields = ["id", "name"]
    search_fields = ["name"]
    pagination_class = CandidatePagination
    filterset_fields = ["mobile_number", "email"]
    permission_classes = [AdminOrReadOnly, IsAuthenticated]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminOrReadOnly, IsAuthenticated]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CallHistoryListView(generics.ListCreateAPIView):
    # queryset = Callhistory.objects.get()
    permission_classes = [AdminOrReadOnly, IsAuthenticated]
    serializer_class = CallHistorySerializer

    def get_queryset(self):
        pk = self.kwargs["candidate_pk"]
        return Callhistory.objects.filter(candidate=pk)
    def perform_create(self, serializer):
        pk = int(self.kwargs.get("candidate_pk"))
        candidate = Candidate.objects.get(id=pk)
        serializer.validated_data["candidate"] = candidate
        serializer.save(candidate=candidate)


class CallHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminOrReadOnly, IsAuthenticated]
    queryset = Callhistory.objects.all()
    serializer_class = CallHistorySerializer

    # FOR THE TIME BEING ADMIN CAN CREATE CALL HISTORY MANNUALLY USIGN API BUT IN FUTURE WE CAN IMPLEMENT CALL SYSTEM TO CREATE CALL HISTORY AUTOMATICALLY
    