from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^blog_posts', views.blog_posts),
	url(r'^$', views.index, name='index'),
]
