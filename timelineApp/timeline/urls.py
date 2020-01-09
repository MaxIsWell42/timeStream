from django.urls import path
from .views import (UserTimelineListView, TimelineDetailView, TimelineUpdateView, TimelineCreateView, TimelineDeleteView, UserTimelineListView)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<str:username>/Timelines', views.UserTimelineListView.as_view(), name='user-Timelines'),
    path('Timeline/<int:pk>/', views.TimelineDetailView.as_view, name='Timeline'),
    path('Timeline/new/', views.TimelineCreateView.as_view, name='new-Timeline'),
    #Trying to make a profile page
    # path('/user/<str:username>/')
]