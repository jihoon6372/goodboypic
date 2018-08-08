from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from portfolio.models import *
from home.lib.parseurl import urlparse, parse_qsl, parse_qs
from django.conf import settings

# Create your views here.

class PortfolioGroupLV(ListView):
	model = Portfolio
	template_name = 'portfolio/portfolio_list.html'
	css_version = 17
	page_title = '포트폴리오 | '+settings.SITE_NAME

	def get_context_data(self, **kwargs):
		ctx = super(PortfolioGroupLV, self).get_context_data(**kwargs)
		ctx['category'] = 'portfolio'
		ctx['css_version'] = self.css_version
		ctx['page_title'] = self.page_title
		return ctx


class PortfolioGroupDV(DetailView):
	model = Portfolio
	template_name = 'portfolio/portfolio_detail.html'

	def get_context_data(self, **kwargs):
		ctx = super(PortfolioGroupDV, self).get_context_data(**kwargs)
		ctx['category'] = 'portfolio'
		ctx['css_version'] = PortfolioGroupLV.css_version
		ctx['youtube_content_id'] = get_youtube_content_id(self.object.link)
		ctx['page_title'] = PortfolioGroupLV.page_title
		return ctx


def get_youtube_content_id(url):
	a = urlparse(url)

	if 'www.youtube.com' in url:
		a = parse_qs(a.query)
		result = a['v'][0]
	else:
		result = a.path.replace('/', '')

	return result
