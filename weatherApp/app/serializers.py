from rest_framework import serializers
from .models import *
from django.conf import settings


class MaxTempSerializer(serializers.ModelSerializer):
	year = serializers.IntegerField(required=False)
	jan = serializers.CharField(required=False, allow_blank=True)
	feb = serializers.CharField(required=False, allow_blank=True)
	mar = serializers.CharField(required=False, allow_blank=True)
	apr = serializers.CharField(required=False, allow_blank=True)
	may = serializers.CharField(required=False, allow_blank=True)
	jun = serializers.CharField(required=False, allow_blank=True)
	jul = serializers.CharField(required=False, allow_blank=True)
	aug = serializers.CharField(required=False, allow_blank=True)
	sep = serializers.CharField(required=False, allow_blank=True)
	octo = serializers.CharField(required=False, allow_blank=True)
	nov = serializers.CharField(required=False, allow_blank=True)
	dec = serializers.CharField(required=False, allow_blank=True)
	win = serializers.CharField(required=False, allow_blank=True)
	spr = serializers.CharField(required=False, allow_blank=True)
	summ = serializers.CharField(required=False, allow_blank=True)
	aut = serializers.CharField(required=False, allow_blank=True)
	ann = serializers.CharField(required=False, allow_blank=True)

	class Meta:
		model = MaxTemp
		fields = '__all__'

	def create(self, validated_data):
		maxTempObj = MaxTemp.objects.create(**validated_data)
		return maxTempObj


class MinTempSerializer(serializers.ModelSerializer):
	year = serializers.IntegerField(required=False)
	jan = serializers.CharField(required=False, allow_blank=True)
	feb = serializers.CharField(required=False, allow_blank=True)
	mar = serializers.CharField(required=False, allow_blank=True)
	apr = serializers.CharField(required=False, allow_blank=True)
	may = serializers.CharField(required=False, allow_blank=True)
	jun = serializers.CharField(required=False, allow_blank=True)
	jul = serializers.CharField(required=False, allow_blank=True)
	aug = serializers.CharField(required=False, allow_blank=True)
	sep = serializers.CharField(required=False, allow_blank=True)
	octo = serializers.CharField(required=False, allow_blank=True)
	nov = serializers.CharField(required=False, allow_blank=True)
	dec = serializers.CharField(required=False, allow_blank=True)
	win = serializers.CharField(required=False, allow_blank=True)
	spr = serializers.CharField(required=False, allow_blank=True)
	summ = serializers.CharField(required=False, allow_blank=True)
	aut = serializers.CharField(required=False, allow_blank=True)
	ann = serializers.CharField(required=False, allow_blank=True)

	class Meta:
		model = MinTemp
		fields = '__all__'

	def create(self, validated_data):
		minTempObj = MinTemp.objects.create(**validated_data)
		return minTempObj


class MeanTempSerializer(serializers.ModelSerializer):
	year = serializers.IntegerField(required=False)
	jan = serializers.CharField(required=False, allow_blank=True)
	feb = serializers.CharField(required=False, allow_blank=True)
	mar = serializers.CharField(required=False, allow_blank=True)
	apr = serializers.CharField(required=False, allow_blank=True)
	may = serializers.CharField(required=False, allow_blank=True)
	jun = serializers.CharField(required=False, allow_blank=True)
	jul = serializers.CharField(required=False, allow_blank=True)
	aug = serializers.CharField(required=False, allow_blank=True)
	sep = serializers.CharField(required=False, allow_blank=True)
	octo = serializers.CharField(required=False, allow_blank=True)
	nov = serializers.CharField(required=False, allow_blank=True)
	dec = serializers.CharField(required=False, allow_blank=True)
	win = serializers.CharField(required=False, allow_blank=True)
	spr = serializers.CharField(required=False, allow_blank=True)
	summ = serializers.CharField(required=False, allow_blank=True)
	aut = serializers.CharField(required=False, allow_blank=True)
	ann = serializers.CharField(required=False, allow_blank=True)

	class Meta:
		model = MeanTemp
		fields = '__all__'


class RainfallSerializer(serializers.ModelSerializer):
	year = serializers.IntegerField(required=False)
	jan = serializers.CharField(required=False, allow_blank=True)
	feb = serializers.CharField(required=False, allow_blank=True)
	mar = serializers.CharField(required=False, allow_blank=True)
	apr = serializers.CharField(required=False, allow_blank=True)
	may = serializers.CharField(required=False, allow_blank=True)
	jun = serializers.CharField(required=False, allow_blank=True)
	jul = serializers.CharField(required=False, allow_blank=True)
	aug = serializers.CharField(required=False, allow_blank=True)
	sep = serializers.CharField(required=False, allow_blank=True)
	octo = serializers.CharField(required=False, allow_blank=True)
	nov = serializers.CharField(required=False, allow_blank=True)
	dec = serializers.CharField(required=False, allow_blank=True)
	win = serializers.CharField(required=False, allow_blank=True)
	spr = serializers.CharField(required=False, allow_blank=True)
	summ = serializers.CharField(required=False, allow_blank=True)
	aut = serializers.CharField(required=False, allow_blank=True)
	ann = serializers.CharField(required=False, allow_blank=True)

	class Meta:
		model = Rainfall
		fields = '__all__'


class SunshineSerializer(serializers.ModelSerializer):
	year = serializers.IntegerField(required=False)
	jan = serializers.CharField(required=False, allow_blank=True)
	feb = serializers.CharField(required=False, allow_blank=True)
	mar = serializers.CharField(required=False, allow_blank=True)
	apr = serializers.CharField(required=False, allow_blank=True)
	may = serializers.CharField(required=False, allow_blank=True)
	jun = serializers.CharField(required=False, allow_blank=True)
	jul = serializers.CharField(required=False, allow_blank=True)
	aug = serializers.CharField(required=False, allow_blank=True)
	sep = serializers.CharField(required=False, allow_blank=True)
	octo = serializers.CharField(required=False, allow_blank=True)
	nov = serializers.CharField(required=False, allow_blank=True)
	dec = serializers.CharField(required=False, allow_blank=True)
	win = serializers.CharField(required=False, allow_blank=True)
	spr = serializers.CharField(required=False, allow_blank=True)
	summ = serializers.CharField(required=False, allow_blank=True)
	aut = serializers.CharField(required=False, allow_blank=True)
	ann = serializers.CharField(required=False, allow_blank=True)

	class Meta:
		model = Sunshine
		fields = '__all__'


class GetMaxTempSerializer(serializers.ModelSerializer):
	class Meta:
		model = MaxTemp
		fields = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octo', 'nov', 'dec']


class GetMinTempSerializer(serializers.ModelSerializer):
	class Meta:
		model = MaxTemp
		fields = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octo', 'nov', 'dec']

class GetMeanTempSerializer(serializers.ModelSerializer):
	class Meta:
		model = MaxTemp
		fields = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octo', 'nov', 'dec']

class GetRainfallSerializer(serializers.ModelSerializer):
	class Meta:
		model = MaxTemp
		fields = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octo', 'nov', 'dec']

class GetSunshineSerializer(serializers.ModelSerializer):
	class Meta:
		model = MaxTemp
		fields = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octo', 'nov', 'dec']