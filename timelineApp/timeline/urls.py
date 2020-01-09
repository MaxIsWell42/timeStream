from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<str:username>', views.UserTimelineListView.as_view(), name='user-timelines'),
]