import json

from django.test import TestCase
from django.urls import reverse


from rest_framework.test import APITestCase

from .models import *
from .serializers import *

# Create your tests here.


class TempModelTestCase(APITestCase):
	# , args=[]
	def setUp(self):
		self.country = "UK"
		self.country_obj = Countries.objects.create(country=self.country)

	def test_maxTemp_model(self):
		self.maxTempObj = MaxTemp.objects.create(
			country = self.country_obj,
			year = 2017,
			jan = 6.3,
			feb = 5.4,
			mar=7.2,
			apr=10.1,
			may=13.6,
			jun=16.4,
			jul=18.0,
			aug=16.7,
			sep=15.3,
			octo=12.3,
			nov=9.1,
			dec=8.4,
			win=5.83,
			spr=10.34,
			summ=17.04,
			aut=12.22,
			ann=11.6
			)
		maxTemp_retrieve=MaxTemp.objects.filter(year=2017).first()
		self.assertEqual(2017, maxTemp_retrieve.year)
		self.assertTrue(1== MaxTemp.objects.count())
		maxTemp_retrieve.delete()
		self.assertTrue(0== MaxTemp.objects.count())

	def test_minTemp_model(self):
		self.minTempObj = MinTemp.objects.create(
			country = self.country_obj,
			year = 2017,
			jan = 6.3,
			feb = 5.4,
			mar=7.2,
			apr=10.1,
			may=13.6,
			jun=16.4,
			jul=18.0,
			aug=16.7,
			sep=15.3,
			octo=12.3,
			nov=9.1,
			dec=8.4,
			win=5.83,
			spr=10.34,
			summ=17.04,
			aut=12.22,
			ann=11.60
			)
		minTemp_retrieve=MinTemp.objects.filter(year=2017).first()
		self.assertEqual(2017, minTemp_retrieve.year)
		self.assertTrue(1== MinTemp.objects.count())
		minTemp_retrieve.delete()
		self.assertTrue(0== MinTemp.objects.count())

	def test_meanTemp_model(self):
		self.meanTempObj = MeanTemp.objects.create(
			country = self.country_obj,
			year = 2017,
			jan = 6.3,
			feb = 5.4,
			mar=7.2,
			apr=10.1,
			may=13.6,
			jun=16.4,
			jul=18.0,
			aug=16.7,
			sep=15.3,
			octo=12.3,
			nov=9.1,
			dec=8.4,
			win=5.83,
			spr=10.34,
			summ=17.04,
			aut=12.22,
			ann=11.60
			)
		mean_retrieve=MeanTemp.objects.filter(year=2017).first()
		self.assertEqual(2017, mean_retrieve.year)
		self.assertTrue(1== MeanTemp.objects.count())
		mean_retrieve.delete()
		self.assertTrue(0== MeanTemp.objects.count())

	def test_rainfall_model(self):
		self.rainfallObj = Rainfall.objects.create(
			country = self.country_obj,
			year = 2017,
			jan = 6.3,
			feb = 5.4,
			mar=7.2,
			apr=10.1,
			may=13.6,
			jun=16.4,
			jul=18.0,
			aug=16.7,
			sep=15.3,
			octo=12.3,
			nov=9.1,
			dec=8.4,
			win=5.83,
			spr=10.34,
			summ=17.04,
			aut=12.22,
			ann=11.60
			)
		rainfall_retrieve=Rainfall.objects.filter(year=2017).first()
		self.assertEqual(2017, rainfall_retrieve.year)
		self.assertTrue(1== Rainfall.objects.count())
		rainfall_retrieve.delete()
		self.assertTrue(0== Rainfall.objects.count())

	def test_sunshine_model(self):
		self.sunshineObj = Sunshine.objects.create(
			country = self.country_obj,
			year = 2017,
			jan = 6.3,
			feb = 5.4,
			mar=7.2,
			apr=10.1,
			may=13.6,
			jun=16.4,
			jul=18.0,
			aug=16.7,
			sep=15.3,
			octo=12.3,
			nov=9.1,
			dec=8.4,
			win=5.83,
			spr=10.34,
			summ=17.04,
			aut=12.22,
			ann=11.60
			)
		sunshine_retrieve=Sunshine.objects.filter(year=2017).first()
		self.assertEqual(2017, sunshine_retrieve.year)
		self.assertTrue(1== Sunshine.objects.count())
		sunshine_retrieve.delete()
		self.assertTrue(0== Sunshine.objects.count())


class TempReadingsAPIViewTestCase(APITestCase):
	url = reverse("app:save_data")

	def test_create_readings(self):
		response = self.client.post(self.url)
		self.assertEqual(201, response.status_code)

class YearListAPIViewTestCase(APITestCase):
	url = reverse("app:get_years")

	def test_list_year(self):
		response = self.client.get(self.url)

		self.assertEqual(200, response.status_code)

class TempReadingsAPIViewGetTestCase(APITestCase):
	url = reverse("app:get_data")

	def test_get_readings(self):
		response = self.client.get(self.url)
		self.assertEqual(200, response.status_code)


