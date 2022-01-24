from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


'''
from django.conf import settings



def get_image_path(instance, filename):
    return settings.MEDIA_ROOT + str(instance.id) + '{}'.format(filename)
'''
# Create your models here.

class Author(models.Model):
	username = models.CharField(max_length=200, default='', unique=True)

	def to_anon(self):
		return Anon.objects.get(username__username=self.username)

class Invoice(models.Model):
	amount = models.IntegerField(default=0)
	item_name = models.CharField(max_length=200, default='', unique=True)
	author = models.CharField(max_length=200, default='', unique=True)
	success = models.BooleanField(default=False)
	submit_date = models.DateTimeField(default=timezone.now)


class Quotation(models.Model):
	compound_or_herb = models.TextField(max_length=1440, default='')
	associated_effect = models.TextField(max_length=1440, default='')
	quote = models.TextField(max_length=1440, default='')
	reference = models.URLField(max_length=2000, blank=True, default='')
	authors = models.TextField(max_length=1440, default='')
	copyright = models.TextField(max_length=1440, default='')

class Change(models.Model):
	quotes = models.ManyToManyField(Quotation, default=None)
	

class Dosage(models.Model):
	quotes = models.ManyToManyField(Quotation, default=None)
	

class Review(models.Model):
	quotes = models.ManyToManyField(Quotation, default=None)
	

class Mechanism(models.Model):
	quotes = models.ManyToManyField(Quotation, default=None)
	

class Function(models.Model):
	quotes = models.ManyToManyField(Quotation, default=None)
	

class Side_Effect(models.Model):
	quotes = models.ManyToManyField(Quotation, default=None)
	


class Compound(models.Model):
	title = models.CharField(max_length=100, default='', unique=True)
	changes = models.OneToOneField(Change, default=None, null=True, on_delete=models.CASCADE)
	dosages = models.OneToOneField(Dosage, default=None, null=True, on_delete=models.CASCADE)
	reviews = models.OneToOneField(Review, default=None, null=True, on_delete=models.CASCADE)
	mechanisms = models.OneToOneField(Mechanism, default=None, null=True, on_delete=models.CASCADE)
	functions = models.OneToOneField(Function, default=None, null=True, on_delete=models.CASCADE)
	side_effects = models.OneToOneField(Side_Effect, default=None, null=True, on_delete=models.CASCADE)

	

class Herb(models.Model):
	title = models.CharField(max_length=100, default='', unique=True)
	changes = models.OneToOneField(Change, default=None, null=True, on_delete=models.CASCADE)
	dosages = models.OneToOneField(Dosage, default=None, null=True, on_delete=models.CASCADE)
	reviews = models.OneToOneField(Review, default=None, null=True, on_delete=models.CASCADE)
	mechanisms = models.OneToOneField(Mechanism, default=None, null=True, on_delete=models.CASCADE)
	functions = models.OneToOneField(Function, default=None, null=True, on_delete=models.CASCADE)
	side_effects = models.OneToOneField(Side_Effect, default=None, null=True, on_delete=models.CASCADE)
	

class Target(models.Model):
	title = models.CharField(max_length=100, default='', unique=True)
	changes = models.OneToOneField(Change, default=None, null=True, on_delete=models.CASCADE)
	dosages = models.OneToOneField(Dosage, default=None, null=True, on_delete=models.CASCADE)
	reviews = models.OneToOneField(Review, default=None, null=True, on_delete=models.CASCADE)
	mechanisms = models.OneToOneField(Mechanism, default=None, null=True, on_delete=models.CASCADE)
	functions = models.OneToOneField(Function, default=None, null=True, on_delete=models.CASCADE)
	side_effects = models.OneToOneField(Side_Effect, default=None, null=True, on_delete=models.CASCADE)
	

class Product(models.Model):
	title = models.CharField(max_length=100, default='', unique=True)
	original = models.IntegerField(default=0)
	seller = models.OneToOneField(Author, default=None, null=True, on_delete=models.CASCADE)
	description = models.TextField(max_length=144000, default='')
	compounds = models.ManyToManyField(Compound, default=None)
	herbs = models.ManyToManyField(Herb, default=None)
	targets = models.ManyToManyField(Target, default=None)
	img = models.URLField(max_length=2000, blank=True, default='')
	price = models.IntegerField(default=0)
	stock = models.IntegerField(default=0)
	sale_qty = models.IntegerField(default=0)
	latest_change_date = models.DateTimeField(default=timezone.now)
	purchases = models.ManyToManyField(Invoice, default=None)

PRODUCT_SORT_CHOICES = ( 
	(0, 'title'),
	(1, '-title'),
	(2, 'description'),
	(3, '-description'),
	(4, 'price'),
	(5, '-price'),
	(6, 'stock'),
	(7, '-stock'),
	(8, 'sale_qty'),
	(9, '-sale_qty'),

)

class Anon(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE)
	whotheysent = models.ManyToManyField(Author, default=None)
	purchases = models.ManyToManyField(Invoice, default=None)
	product_sort = models.IntegerField(choices=PRODUCT_SORT_CHOICES, default=0)
	last_login_date = models.DateTimeField(default=timezone.now)
	
	cart = models.ManyToManyField(Product, default=None)

	def __unicode__(self):
		return unicode(self.username) or u''