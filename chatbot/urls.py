from django.urls import re_path, path
from .views import request_answer_view

urlpatterns = [
    # re_path('^', UserListCreate.as_view(), name='chatbot'),
    path('chatbot_api/', request_answer_view, name='chatbot-api'),
    # path('users/', UserListCreate.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]