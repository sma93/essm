from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse #used for tutorial
from django.http import JsonResponse
import sdbee, sdbee1

#TODO: add views for the other static html pages (about, archive etc)
def index(request):
	return render(request, "index.html", {})

def about(request):
	return render(request, "about.html", {})

def archives(request):
	return render(request, "archives.html", {})

def links(request):
	return render(request, "links.html", {})

def contact(request):
	return render(request, "contact.html", {})

@ensure_csrf_cookie
def post_page(request):
	return render(request, "post.html", {})

# TODO: clearer name would be blog_content, or articles
def blog_posts(request):
	if(request.method == "POST"):
		resp = sdbee.save_post(request.POST.get('title'), request.POST.get('author'), request.POST.get('text'))
	else:
		resp = sdbee.get_posts()
	return JsonResponse(resp)

def dummy(request):
	d = {'test': 'fake'}
	return JsonResponse(d);

def comments(request):
	if(request.method == "COMMENT"):
		resp1 = sdbee1.save_post(request.COMMENT.get('text'))
	else:
		resp1 = sdbee1.get_posts()
	return JsonResponse(resp1)
