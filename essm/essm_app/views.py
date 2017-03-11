from django.shortcuts import render
from django.http import HttpResponse #used for tutorial
from django.http import JsonResponse
import sdbee

# Create your views here.
def index(request):
	return render(request, "index.html", {})
	#return HttpResponse("This is a test. to be replaced by index view")

def blog_posts(request):
	resp = sdbee.sdb_blog_posts()
	return JsonResponse(resp)