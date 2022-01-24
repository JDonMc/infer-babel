# Copyright Aden Handasyde 2019

from django.conf.urls import url
from . import views
from . import models
from django.contrib import admin

# admin.site.register(models.Sponsor)
# ^^^^ Use for cleaning up dodgy datatables


# Each has a sort
# Needs a page-number
urlpatterns = [
	# url(r'^admin/', admin.site.urls),
	url(r'^logout/$', views.logout_user, name='logout_user'),
	url(r'^login/$', views.login_view, name='login_view'),
	url(r'^owner/$', views.owner, name='owner'),
	url(r'^feedback/$', views.feedback, name='feedback'),
	url(r'^create_feedback/$', views.create_feedback, name='create_feedback'),
	url(r'^thanks/$', views.thanks, name='thanks'),
	url(r'^about/$', views.about, name='about'),
	url(r'^register/$', views.register_view, name='register_view'),
	url(r'^change_sort/(?P<sort>[\w-]+)/$', views.change_sort, name='change_sort'),
	url(r'^approve_compound/(?P<compound>[\w-]+)/$', views.approve_compound, name='approve_compound'),
	url(r'^approve_herb/(?P<herb>[\w-]+)/$', views.approve_herb, name='approve_herb'),
	url(r'^approve_target/(?P<target>[\w-]+)/$', views.approve_target, name='approve_target'),
	url(r'^approve_mix/(?P<target>[\w-]+)/(?P<compound>[\w-]+)/(?P<herb>[\w-]+)/$', views.approve_mix, name='approve_mix'),
	url(r'^admin/$', views.admin, name='admin'),
	url(r'^delete_product/(?P<product>[\w-]+)/$', views.delete_product, name='delete_product'),
	url(r'^index/$', views.index, name='index'),
	url(r'^cart/(?P<failure>[\w-]+)/$', views.cart, name='cart'),
	url(r'^products/(?P<title>[\w-]+)/seller/(?P<seller>[\w-]+)/$', views.products, name='products'),
	url(r'^requantify_product/(?P<title>[\w-]+)/(?P<qty>[\w-]+)/$', views.index, name='index'),
]