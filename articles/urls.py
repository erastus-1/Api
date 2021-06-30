from django.urls import path
from .views import *

urlpatterns = [
    path('api/all/', ArticlePostView.as_view(), name='articles'),
    path('api/post/', ArticlePostView.as_view(), name='article_post'),
    path('api/update/<int:pk>/', ArticlePostView.as_view(), name='update_post'),
]