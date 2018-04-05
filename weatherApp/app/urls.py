from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^save_data', views.DataSaveView.as_view(), name='save_data'),
	url(r'^get_data/$', views.GetDataView.as_view(), name='get_data'),
	url(r'^get_data/(?P<country>\w{0,50})/(?P<year>[0-9]+)$', views.GetDataView.as_view(), name='get_data_country_year'),
	url(r'^get_data/(?P<country>\w{0,50})$', views.GetDataView.as_view()),
	url(r'^get_years', views.GetYearView.as_view(), name='get_years'),
	
]