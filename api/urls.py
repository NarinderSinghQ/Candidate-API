
from django.urls import path 
from . views import *
urlpatterns = [
    path('candidates/' , CandidateListView.as_view() , name = 'candidate-list'),
    path('candidates/<int:pk>/' , CandidateDetailView.as_view() , name = 'candidate-detail'),
    path('candidates/<int:candidate_pk>/call-logs/' , CallHistoryListView.as_view() , name = 'calllog-list'),
    # path('candidates/<int:pk1>/call-history/<int:pk>/' , CallHistoryDetailView.as_view() , name = 'callHistory-detail'),
    path('candidates/<int:candidate_pk>/call-logs/<int:pk>/', CallHistoryDetailView.as_view(), name='calllog-detail'),

]

