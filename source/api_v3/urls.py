from django.urls import path
from api_v3.views import json_echo_view, get_token_view, ArticleView

app_name = 'api_v3'

urlpatterns = [
    path('echo/', json_echo_view, name = 'echo'),
    path('token/', get_token_view, name = 'get_token'),
    path('article/', ArticleView.as_view(), name='article'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_detail')
]