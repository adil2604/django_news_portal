from django.urls import path

from .views import NewsAPI,NewsAddAPI

urlpatterns = [
    path('news/', NewsAPI.as_view()),
    path('news/add/', NewsAddAPI.as_view()),

]
