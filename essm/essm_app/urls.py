from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	url(r'^blog_posts', views.blog_posts),
	url(r'^post', views.post_page),
	url(r'^dummy', views.dummy),
	url(r'^$', views.index, name='index'),
] + staticfiles_urlpatterns()
