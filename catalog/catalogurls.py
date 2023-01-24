from django.urls import path

from catalog.apps import MyappConfig
from catalog.views import hello

appname = MyappConfig.name

urlpatterns = [
    path('', hello)
]