from django.urls import path
from workflow.views import *

app_name = 'workflow';

urlpatterns = [
    path('', workflowIndex.as_view(), name='index'),
]