# from django.conf.urls import url, include
from django.urls import path, include
from history.views import *

app_name = "history"

urlpatterns = [
    path('', historyIndex.as_view(), name='index'),
    # url(r'^test/', testIndex.as_view())
]