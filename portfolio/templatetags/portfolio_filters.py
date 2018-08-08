from django import template
from home.lib.parseurl import urlparse, parse_qsl, parse_qs

register = template.Library()

@register.filter('youtube_thumb_url')
def youtube_thumb_url(url):
	if url:
		thumb_url = "https://i.ytimg.com/vi/"+get_youtube_content_id(url)+"/0.jpg"
	else:
		thumb_url = ''
	
	return thumb_url


@register.filter('get_youtube_content_id')
def get_youtube_content_id(url):
	a = urlparse(url)

	if 'www.youtube.com' in url:
		a = parse_qs(a.query)
		result = a['v'][0]
	else:
		result = a.path.replace('/', '')

	return result


@register.filter('year_position')
def year_position(year_id, _type):
	if 'line' in _type:
		if year_id%2==0:
			return "left"
		else:
			return "right"
	elif 'circle' in _type:
		if year_id%2==0:
			return "right"
		else:
			return "left"
	else:
		if year_id%2==0:
			return "right"
		else:
			return "left"