from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse #used for tutorial
from django.http import JsonResponse
import sdbee

# Create your views here.
def index(request):
	return render(request, "index.html", {})
	#return HttpResponse("This is a test. to be replaced by index view")

@ensure_csrf_cookie
def post_page(request):
	return render(request, "post.html", {})

def blog_posts(request):
	if(request.method == "POST"):
		resp = sdbee.save_post(request.POST.get('title'), request.POST.get('author'), request.POST.get('text'))
	else:
		resp = sdbee.get_posts()
	return JsonResponse(resp)

def dummy(request):
	d = {'test': 'fake'}
	return JsonResponse(d);