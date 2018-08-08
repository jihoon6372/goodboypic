from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.http import response
from django.http import HttpResponse
from history.models import History
from portfolio.models import PortfolioGroup
from django.conf import settings

# Create your views here.

class historyIndex(ListView):
	model = PortfolioGroup
	context_object_name = 'historyIndex'
	template_name = 'history/history_index.html'
	css_version = 8
	ordering = ['name']
	page_title = '연혁 | '+settings.SITE_NAME

	# def get(self, request, *args, **kwargs):
	# 	context = self.get_context_data(**kwargs)
	# 	response = self.render_to_response(context)
	# 	response.set_cookie('test2', 'tetete3')
	# 	return response

	def get_context_data(self, **kwargs):
		ctx = super(historyIndex, self).get_context_data(**kwargs)
		ctx['category'] = 'history'
		ctx['css_version'] = self.css_version
		ctx['page_title'] = self.page_title

		return ctx


class testIndex(ListView):
	model = History
	template_name = 'history/test.html'
		