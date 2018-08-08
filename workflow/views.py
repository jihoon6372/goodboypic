from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings

# Create your views here.
class workflowIndex(TemplateView):
	template_name = 'workflow/workflow_index.html'
	css_version = 10

	def get_context_data(self, **kwargs):
		ctx = super(workflowIndex, self).get_context_data(**kwargs)
		ctx['category'] = 'workflow'
		ctx['css_version'] = self.css_version
		ctx['page_title'] = settings.SITE_NAME

		return ctx