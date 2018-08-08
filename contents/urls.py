from django.urls import re_path, path
from .views import *

app_name = 'contents'

urlpatterns = [
    # Example : /
    path('', ContentsLV.as_view(), name='index'),
    re_path('(?P<slug>[-\w]+)/$', ContentsDV.as_view(), name='detail'),
    # url(r'^portfolio-group/(?P<pk>\d+)/$', PortfolioGroupLV.as_view(), name='portfolio_group_detail'),
]