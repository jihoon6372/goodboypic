from django.urls import path
from qna.views import *

app_name = 'qna'

urlpatterns = [
    path('', qna_new.as_view(), name='index'),
    path('completion/', qnaComp.as_view(), name='comp'),
]