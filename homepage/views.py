# Create your views here.
from django.http import *
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.template import RequestContext
from blogs.models import Blogpost
def main(request):
	posts = Blogpost.objects.all().order_by("-created")
	paginator = Paginator(posts, 2)
	try: 
		page = int(request.GET.get("page", '1'))
	except ValueError: page = 1
	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)
	t=get_template('home.html')
	c=RequestContext(request, {'posts': posts})
	html=t.render(c)
	return HttpResponse(html)