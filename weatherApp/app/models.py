from django.db import models
import datetime


class Countries(models.Model):
	country = models.CharField(max_length=50)

	def __str__(self):
		return self.country 

class MaxTemp(models.Model):
	country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True, related_name='contryMaxTemp')
	year = models.IntegerField(null=True, blank=True)
	jan = models.CharField(max_length=50, null=True, blank=True)
	feb = models.CharField(max_length=50, null=True, blank=True)
	mar = models.CharField(max_length=50, null=True, blank=True)
	apr = models.CharField(max_length=50, null=True, blank=True)
	may = models.CharField(max_length=50, null=True, blank=True)
	jun = models.CharField(max_length=50, null=True, blank=True)
	jul = models.CharField(max_length=50, null=True, blank=True)
	aug = models.CharField(max_length=50, null=True, blank=True)
	sep = models.CharField(max_length=50, null=True, blank=True)
	octo = models.CharField(max_length=50, null=True, blank=True)
	nov = models.CharField(max_length=50, null=True, blank=True)
	dec = models.CharField(max_length=50, null=True, blank=True)
	win = models.CharField(max_length=50, null=True, blank=True)
	spr = models.CharField(max_length=50, null=True, blank=True)
	summ = models.CharField(max_length=50, null=True, blank=True)
	aut = models.CharField(max_length=50, null=True, blank=True)
	ann = models.CharField(max_length=50, null=True, blank=True)




class MinTemp(models.Model):
	country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True, related_name='contryMinTemp')
	year = models.IntegerField(null=True, blank=True)
	jan = models.CharField(max_length=50, null=True, blank=True)
	feb = models.CharField(max_length=50, null=True, blank=True)
	mar = models.CharField(max_length=50, null=True, blank=True)
	apr = models.CharField(max_length=50, null=True, blank=True)
	may = models.CharField(max_length=50, null=True, blank=True)
	jun = models.CharField(max_length=50, null=True, blank=True)
	jul = models.CharField(max_length=50, null=True, blank=True)
	aug = models.CharField(max_length=50, null=True, blank=True)
	sep = models.CharField(max_length=50, null=True, blank=True)
	octo = models.CharField(max_length=50, null=True, blank=True)
	nov = models.CharField(max_length=50, null=True, blank=True)
	dec = models.CharField(max_length=50, null=True, blank=True)
	win = models.CharField(max_length=50, null=True, blank=True)
	spr = models.CharField(max_length=50, null=True, blank=True)
	summ = models.CharField(max_length=50, null=True, blank=True)
	aut = models.CharField(max_length=50, null=True, blank=True)
	ann = models.CharField(max_length=50, null=True, blank=True)


class MeanTemp(models.Model):
	country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True, related_name='contryMeanTemp')
	year = models.IntegerField(null=True, blank=True)
	jan = models.CharField(max_length=50, null=True, blank=True)
	feb = models.CharField(max_length=50, null=True, blank=True)
	mar = models.CharField(max_length=50, null=True, blank=True)
	apr = models.CharField(max_length=50, null=True, blank=True)
	may = models.CharField(max_length=50, null=True, blank=True)
	jun = models.CharField(max_length=50, null=True, blank=True)
	jul = models.CharField(max_length=50, null=True, blank=True)
	aug = models.CharField(max_length=50, null=True, blank=True)
	sep = models.CharField(max_length=50, null=True, blank=True)
	octo = models.CharField(max_length=50, null=True, blank=True)
	nov = models.CharField(max_length=50, null=True, blank=True)
	dec = models.CharField(max_length=50, null=True, blank=True)
	win = models.CharField(max_length=50, null=True, blank=True)
	spr = models.CharField(max_length=50, null=True, blank=True)
	summ = models.CharField(max_length=50, null=True, blank=True)
	aut = models.CharField(max_length=50, null=True, blank=True)
	ann = models.CharField(max_length=50, null=True, blank=True)


class Rainfall(models.Model):
	country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True, related_name='contryRainfall')
	year = models.IntegerField(null=True, blank=True)
	jan = models.CharField(max_length=50, null=True, blank=True)
	feb = models.CharField(max_length=50, null=True, blank=True)
	mar = models.CharField(max_length=50, null=True, blank=True)
	apr = models.CharField(max_length=50, null=True, blank=True)
	may = models.CharField(max_length=50, null=True, blank=True)
	jun = models.CharField(max_length=50, null=True, blank=True)
	jul = models.CharField(max_length=50, null=True, blank=True)
	aug = models.CharField(max_length=50, null=True, blank=True)
	sep = models.CharField(max_length=50, null=True, blank=True)
	octo = models.CharField(max_length=50, null=True, blank=True)
	nov = models.CharField(max_length=50, null=True, blank=True)
	dec = models.CharField(max_length=50, null=True, blank=True)
	win = models.CharField(max_length=50, null=True, blank=True)
	spr = models.CharField(max_length=50, null=True, blank=True)
	summ = models.CharField(max_length=50, null=True, blank=True)
	aut = models.CharField(max_length=50, null=True, blank=True)
	ann = models.CharField(max_length=50, null=True, blank=True)


class Sunshine(models.Model):
	country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True, related_name='contrySunshine')
	year = models.IntegerField(null=True, blank=True)
	jan = models.CharField(max_length=50, null=True, blank=True)
	feb = models.CharField(max_length=50, null=True, blank=True)
	mar = models.CharField(max_length=50, null=True, blank=True)
	apr = models.CharField(max_length=50, null=True, blank=True)
	may = models.CharField(max_length=50, null=True, blank=True)
	jun = models.CharField(max_length=50, null=True, blank=True)
	jul = models.CharField(max_length=50, null=True, blank=True)
	aug = models.CharField(max_length=50, null=True, blank=True)
	sep = models.CharField(max_length=50, null=True, blank=True)
	octo = models.CharField(max_length=50, null=True, blank=True)
	nov = models.CharField(max_length=50, null=True, blank=True)
	dec = models.CharField(max_length=50, null=True, blank=True)
	win = models.CharField(max_length=50, null=True, blank=True)
	spr = models.CharField(max_length=50, null=True, blank=True)
	summ = models.CharField(max_length=50, null=True, blank=True)
	aut = models.CharField(max_length=50, null=True, blank=True)
	ann = models.CharField(max_length=50, null=True, blank=True)
