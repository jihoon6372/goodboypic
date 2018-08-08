from .models import AuthLog
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class AuthLogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if 'is_authenticated' not in request.session:
            request.session['is_authenticated'] = False

        if '_auth_user_id' in request.session:
            if request.session['is_authenticated'] != request.session['_auth_user_id']:
                a = AuthLog()
                a.user_id = request.user.id
                a.ip_address = request.META.get('REMOTE_ADDR', '')
                a.user_agent = request.META.get('HTTP_USER_AGENT', '')
                a.save()

                request.session['is_authenticated'] = request.session['_auth_user_id']
                return None