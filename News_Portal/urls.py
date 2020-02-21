
from django.contrib import admin
from django.urls import path,include
from news.views import index
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/v1/', include('news.urls')),

]
