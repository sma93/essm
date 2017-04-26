from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	url(r'^blog_posts', views.blog_posts),
	url(r'^post', views.post_page),
	url(r'^dummy', views.dummy),
	url(r'^$', views.index, name='index'),
	url(r'^home', views.index, name='index'),
	url(r'^archives', views.archives),
	url(r'^about', views.about),
	url(r'^links', views.links),
	url(r'^contact', views.contact),
] + staticfiles_urlpatterns()
