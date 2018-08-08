from django.urls import path, re_path
from portfolio.views import *
from django.http import HttpResponse

app_name = "portfolio"

urlpatterns = [
    path('', PortfolioGroupLV.as_view(), name='index'),
    re_path('(?P<slug>[\w-]+)/', PortfolioGroupDV.as_view(), name='portfolio_detail'),
    # path('<slug:slug>/', PortfolioGroupDV.as_view(), name='portfolio_detail'),
    # url(r'^portfolio-group/(?P<pk>\d+)/$', PortfolioGroupLV.as_view(), name='portfolio_group_detail'),
]