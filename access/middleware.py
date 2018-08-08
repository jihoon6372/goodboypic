from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from .models import BlockIP, DevModeAllowIP
from django.conf import settings

Http403 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
    <title>403 ERROR: Access denied</title>
</head>
<body>
    <h1>Access Denied (403)</h1>
    We're sorry, but you are not authorized to view this page.
</body>
</html>"""

# 접속 차단
class BlockIPMiddleware(MiddlewareMixin):

	def process_request(self, request):
		if BlockIP.objects.filter(ip_address=request.META.get('REMOTE_ADDR')).count() > 0:
			return HttpResponseForbidden(Http403)
		
		return None


# 개발자 모드 일때 접속 허용
class DevModeAllowIPMiddleware(MiddlewareMixin):
	
	def process_request(self, request):
		request.session['debug_mode'] = settings.DEBUG
		Http_dev = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
    <title>사이트 점검중</title>
</head>
<style type="text/css">
	.check_img{
		margin-top: 10vw;
		text-align: center;
		height: 10vw;
		background: url(/static/images/site_check.png) 50% no-repeat;
		background-size: auto 10vw;
	}

	.check_message:before{
		text-align: center;
		font-size: 2vw;
		content: "사이트 점검중입니다.";
		display: inherit;
	}

	@media screen and (max-width:1024px) {
		.check{
			position: absolute;
			width: 70vw;
			top: 50%;
			margin-top: -400px;
			left: 50%;
			margin-left: -345px;
		}

		.check_img{
			background-size: auto 50vw;
			margin-top: 0;
			height: 50vw;
		}

		.check_message:before{
			font-size: 6vw;
		}
	}
</style>
<body>
	<div class="check">
		<div class="check_img"></div>
		<div class="check_message"></div>
	</div>
</body>
</html>"""
		if DevModeAllowIP.objects.filter(ip_address=request.META.get('REMOTE_ADDR')).count() == 0 and settings.DEBUG:
			return HttpResponseForbidden(Http_dev)
		
		return None