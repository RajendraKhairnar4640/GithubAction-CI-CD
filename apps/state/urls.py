from django.urls import path
from apps.state.views import index


urlpatterns = [
    path('index/', index, name='index'),
]
