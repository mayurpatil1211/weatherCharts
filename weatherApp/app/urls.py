from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^save_data', views.save_data),
	url(r'^get_data/$', views.get_data),
	url(r'^get_data/(?P<country>\w{0,50})/(?P<year>[0-9]+)$', views.get_data),
	url(r'^get_data/(?P<country>\w{0,50})$', views.get_data),
	url(r'^get_years', views.get_year),
	
]