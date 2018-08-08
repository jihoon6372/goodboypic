from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from qna.models import Qna
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.base import TemplateView

from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from qna.forms import QnaForm
from django.contrib.humanize.templatetags.humanize import intcomma
from django.conf import settings

# Create your views here.
class qnaComp(TemplateView):
	template_name = 'qna/qna_comp.html'

	def get_context_data(self, **kwargs):
		ctx = super(qnaComp, self).get_context_data(**kwargs)
		ctx['category'] = 'qna'
		ctx['css_version'] = qna_new.css_version
		ctx['page_title'] = settings.SITE_NAME

		if 'qna_success' in self.request.session:
			del(self.request.session['qna_success'])
		else:
			raise Http404 

		return ctx


class qna_new(CreateView):
	model = Qna
	template_name = 'qna/qna_form.html'
	form_class = QnaForm
	success_url = reverse_lazy('qna:comp')
	css_version = 14

	def form_valid(self, form):
		self.request.session['qna_success'] = 'success'
		mail_send(self.request)
		return super(qna_new, self).form_valid(form)

	def get_context_data(self, **kwargs):
		ctx = super(qna_new, self).get_context_data(**kwargs)
		ctx['category'] = 'qna'
		ctx['css_version'] = self.css_version
		ctx['page_title'] = settings.SITE_NAME

		return ctx

def mail_send(request):
	subject = request.POST.get('subject')
	name = request.POST.get('name')
	email = request.POST.get('email')
	message = request.POST.get('content')
	message = message.replace('\n', '<br>')
	budget = intcomma(request.POST.get('budget'), False)

	content = '<div style="width: 500px;">'
	content += '<div><span style="font-weight: bold; display:inline-block; width: 100px;">이름 : </span><span>'+name+'</span></div>'
	content += '<div style="margin-top: 10px;"><span style="font-weight: bold; display:inline-block; width: 100px;">이메일 : </span><span>'+email+'</span></div>'
	content += '<div style="margin-top: 10px;"><span style="font-weight: bold; display:inline-block; width: 100px;">예산 : </span><span>'+budget+'원</span></div>'
	content += '<div style="margin-top: 30px;">'+message+'</div>'
	content += '</div>'

	from_email, to = 'goodboy-pictures@goodboypic.co.kr', 'goodboypic@gmail.com'
	# from_email, to = 'goodboy-pictures@goodboypic.co.kr', 'jihoon6372@gmail.com'
	text_content = 'This is an important message.'
	html_content = '<p>This is an <strong>important</strong> message.</p>'

	msg = EmailMultiAlternatives(subject, content, from_email, [to])
	msg.attach_alternative(content, "text/html")
	msg.send()

	return redirect('qna:comp')