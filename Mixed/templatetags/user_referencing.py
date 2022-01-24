import random
from django import template
from django.urls import reverse
from datetime import datetime
from urllib.parse import quote_plus


register = template.Library()



@register.filter(is_safe=True)
def multiple(stock, price):
	return stock*price

@register.filter(is_safe=True)
def pubmed_url(value):
	import re
	text = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', 'R', value, flags=re.MULTILINE)
	return text

