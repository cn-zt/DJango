from django.urls import path
from . import views

urlpatterns = [
    path('past/', views.vote_past, name='vote_past'),
    path('present/', views.vote_present, name='vote_present'),
    path('future/', views.vote_future, name='vote_future'),
    path('submit_votes/<str:question_type>/', views.submit_votes, name='submit_votes'),
]
