from django.urls import path
from .views import *

urlpatterns = [
    path('',PostViev.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('review/<int:pk>/', AddComments.as_view(),name = 'add_comments')
]