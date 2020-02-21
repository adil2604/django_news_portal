from django.shortcuts import render
from rest_framework import generics

from news.models import News
from .serializers import NewsSerializer


# Create your views here.
class NewsAPI(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsAddAPI(generics.CreateAPIView):
    serializer_class = NewsSerializer


def index(request):
    return render(request,'html.html')

