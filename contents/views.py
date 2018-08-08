from django.shortcuts import render
from django.views.generic import ListView, DetailView
from contents.models import *
from portfolio.views import get_youtube_content_id, PortfolioGroupLV
from django.conf import settings

# Create your views here.

class ContentsLV(ListView):
	model = ContentsType
	template_name = 'contents/contents_list.html'
	css_version = PortfolioGroupLV.css_version
	page_title = '쉼표 | '+settings.SITE_NAME

	def get_context_data(self, **kwargs):
		ctx = super(ContentsLV, self).get_context_data(**kwargs)
		ctx['page_title'] = self.page_title
		ctx['category'] = 'contents'
		ctx['css_version'] = self.css_version
		return ctx


class ContentsDV(DetailView):
	model = Contents
	template_name = 'portfolio/portfolio_detail.html'

	def get_context_data(self, **kwargs):
		ctx = super(ContentsDV, self).get_context_data(**kwargs)
		ctx['page_title'] = ContentsLV.page_title
		ctx['category'] = 'contents'
		ctx['css_version'] = PortfolioGroupLV.css_version
		ctx['youtube_content_id'] = get_youtube_content_id(self.object.link)
		return ctx