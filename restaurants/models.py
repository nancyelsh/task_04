from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()

	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg
		