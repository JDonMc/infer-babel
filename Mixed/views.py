from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.conf import settings

from django.utils import timezone
from .forms import *
from .models import *

# Create your views here.
def logout_user(request):
	user = request.user
	logout(request)
	return redirect('index')

def login_view(request):
	loginform = AuthenticationForm(data=request.POST)
	if loginform.is_valid():
		user = loginform.get_user()
		login(request, user)
	

	### Input redirect to previous page.

	return redirect('index')

def order_products(products, user):
	if user.product_sort == 0:
		return products.order_by('title')
	elif user.product_sort == 1:
		return products.order_by('-title')
	elif user.product_sort == 2:
		return products.order_by('description')
	elif user.product_sort == 3:
		return products.order_by('-description')
	elif user.product_sort == 4:
		return products.order_by('price')
	elif user.product_sort == 5:
		return products.order_by('-price')
	elif user.product_sort == 6:
		return products.order_by('stock')
	elif user.product_sort == 7:
		return products.order_by('-stock')
	elif user.product_sort == 8:
		return products.order_by('sale_qty')
	elif user.product_sort == 9:
		return products.order_by('-sale_qty')
	return products.order_by('sale_qty')

@login_required
def change_sort(request, sort):
	registerform = UserCreationForm()
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	loginform = AuthenticationForm()
	loggedinuser = User.objects.get(username=request.user.username)
	loggedinanon = Anon.objects.get(username=loggedinuser)
	loggedinanon.product_sort = int(sort)
	
	return redirect('index')

from .scihub import SciHub

def search(query):
    

    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    return results


def pdf_reader():

	import PyPDF2 
	import textract
	from nltk.tokenize import word_tokenize
	from nltk.corpus import stopwords


	#write a for-loop to open many files -- leave a comment if you'd #like to learn how
	filename = 'enter the name of the file here' 
	#open allows you to read the file
	pdfFileObj = open(filename,'rb')
	#The pdfReader variable is a readable object that will be parsed
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	#discerning the number of pages will allow us to parse through all #the pages
	num_pages = pdfReader.numPages
	count = 0
	text = ""
	#The while loop will read each page
	while count < num_pages:
	    pageObj = pdfReader.getPage(count)
	    count +=1
	    text += pageObj.extractText()
	#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
	if text != "":
	   text = text
	#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
	else:
	   text = textract.process(fileurl, method='tesseract', language='eng')
	# Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
	# Now, we will clean our text variable, and return it as a list of keywords.
	# Step 3: Convert text into keywords
	#The word_tokenize() function will break our text phrases into #individual words
	tokens = word_tokenize(text)
	#we'll create a new list which contains punctuation we wish to clean
	punctuations = ['(',')',';',':','[',']',',']
	#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
	stop_words = stopwords.words('english')
	#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
	keywords = [word for word in tokens if not word in stop_words and not word in punctuations]


	
	return None

@login_required
def approve_compound(request, compound):
	results = search(compound)
	id_list = results['IdList']
	papers = fetch_details(id_list)
	for i, paper in enumerate(papers['PubmedArticle']):
		if compound in paper['MedlineCitation']['Article']['ArticleTitle']:
			for article in paper['MedlineCitation']['Article']:
				print(article)
	if len(papers['PubmedArticle']) == 200:
		print('be more specific')


	#import pubchempy as pcp
	#compound = pcp.get_compounds(compound, name)
	

	return redirect('admin')

@login_required
def approve_target(request, target):
	Product.objects.create(title="Coming Soon " + target)
	return redirect('admin')

@login_required
def approve_mix(request, target, compound, herb):
	count = 0
	title = 'Coming Soon - '
	description = ' Combined Target, Compound, Herb Approach'
	price = 0
	for product in Product.objects.all():
		if target != 0:
			if target in product.title:
				target_product = product
				url = product.img
		if compound != 0:
			if compound in product.title:
				compound_product = product
				url = product.img
		if herb != 0:
			if herb in product.title:
				herb_product = product
				url = product.img
		count += int(product.description.split(" ")[0])
		title += product.title[0:10] + '... - '
		description += '/n/n' + product.description
		price += product.price
	Product.objects.create(title=title, description=count+description, img=url, price=price, stock=0)
	return redirect('admin')

@login_required
def approve_herb(request, herb):
	Product.objects.create(title="Coming Soon " + herb)
	return redirect('admin')

@login_required
def admin(request):


	registerform = UserCreationForm()
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	loginform = AuthenticationForm()
	loggedinuser = User.objects.get(username=request.user.username)
	loggedinanon = Anon.objects.get(username=loggedinuser)
	if request.user.username == 'home':
		products = Product.objects.all()
		product_form = ProductForm()
		if request.method == 'POST':
			product_form = ProductForm(request.POST)

			if product_form.is_valid():
				Product.objects.create(title=product_form.cleaned_data['title'], description=product_form.cleaned_data['description'], img=product_form.cleaned_data['img'], price=product_form.cleaned_data['price'], stock=product_form.cleaned_data['stock'], )
			print(product_form.errors)
		return render(request, 'admin.html', {"loggedinanon": loggedinanon, "products": products, "product_form": product_form, 'loginform': loginform, 'registerform': registerform})
	return redirect('index')

@login_required
def requantify_product(request, title, qty):
	registerform = UserCreationForm()
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	loginform = AuthenticationForm()
	loggedinuser = User.objects.get(username=request.user.username)
	loggedinanon = Anon.objects.get(username=loggedinuser)
	qty = int(qty)
	if qty == 0:
		loggedinanon.products.get(title=title).delete()
	else:
		loggedinanon.products.get(title=title).stock = qty
	return redirect('cart')

@login_required
def delete_product(request, product):
	Product.objects.get(id=int(product)).delete()
	if request.user.username == 'home':
		return redirect('admin')
	return redirect('cart', failure=0)

def products(request, title, seller):
	registerform = UserCreationForm()
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	loginform = AuthenticationForm()
	product = Product.objects.get(id=title, original=0)
	
	if seller == '0':
		seller = 0
	else:
		sellerauthor = Author.objects.get(username=seller)
		
	qty_form = QtyForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		if request.method == 'POST':
			qty_form = QtyForm(request.POST)
			if qty_form.is_valid():
				if seller != 0:
					buying = Product.objects.create(seller=sellerauthor, title=product.title, description=product.description, img=product.img, price=product.price, stock=qty_form.cleaned_data['stock'])
				else:
					buying = Product.objects.create(title=request.user.username+"'s "+product.title, description=product.description, img=product.img, price=product.price, stock=qty_form.cleaned_data['stock'])
				product.stock -= qty_form.cleaned_data['stock']
				product.save()
				loggedinanon.cart.add(buying)
				loggedinanon.save()
				return redirect('cart', failure=0)
			print(qty_form.errors)
	
	return render(request, 'product.html', {"product": product, "qty_form": qty_form, "seller": seller, 'loginform': loginform, 'registerform': registerform, 'registerterms': registerterms})



@login_required
def user_baking(request, invoice):
	registerform = UserCreationForm()
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinauthor = Author.objects.get(username=request.user.username)
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		invoice = int(invoice)
		if Invoice.objects.get(id=invoice):
			authors_invoice = Invoice.objects.get(id=invoice)
			if int(request.POST.get('invoice')) == invoice:
				authors_invoice.success = True
				authors_invoice.save()
				loggedinauthor.purchases.add(authors_invoice)
				for product in loggedinanon.cart.all():
					if product.seller:
						selleranon = Anon.objects.get(username=User.objects.get(username=product.seller))
						freebie = Product.objects.create(title=product.title, seller=Anon.objects.get(username=User.objects.get(username=loggedinanon)), price=0, stock=1)
						selleranon.cart.add(freebie)
						selleranon.save()
					loggedinanon.cart.remove(product)
					loggedinanon.save()


	return base_redirect(request, 0)

@login_required
def cart(request):
	registerform = UserCreationForm()
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	loginform = AuthenticationForm()
	
	price = 25
	title = ''
	for product in loggedinanon.cart.all():
		price += product.sale_qty * product.price
		title += product.title + ", "
	bread_invoice = Invoice.objects.create(amount=price, item_name=title, author=request.user.username)
	paypal_dict = {
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'amount': '%.2f' % price,
		'item_name': 'Mixed {}, Author {}'.format(price, request.user.username),
		'invoice': str(bread_invoice.id),
		'currency_code': 'AUD',
		'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
		'return_url': 'http://{}{}'.format(host, redirect('user_baking', invoice=bread_invoice.id)),
		'cancel_return': 'http://{}{}'.format(host, redirect('cart', failure=1)),
	}
	paypalform = PayPalPaymentsForm(initial=paypal_dict)
	return render(request, 'cart.html', {"loggedinanon": loggedinanon, "failure": failure, "paypalform": paypalform})


def index(request):
	registerform = UserCreationForm()
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	loginform = AuthenticationForm()
	
	for user in Anon.objects.all():
		for product in user.cart.all():
			pro = 1
			# greater than 1 day, return products to products.
			#if product.latest_change_date > timezone.timedelta(1 day)
			# Product.objects.get(title=product.title, original=0).stock += product.stock
			# product.delete()

	products_by_sold = Product.objects.all().order_by('-sale_qty')

	
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		products_by_sort = order_products(Product.objects.all(), loggedinanon)
		the_response = render(request, 'index.html', {"products": products_by_sort, "loggedinanon": loggedinanon})
	else:
		the_response = render(request, 'index.html', {"products": products_by_sold, 'loginform': loginform, 'registerform': registerform, 'registerterms': registerterms})
	
	the_response.set_cookie('current', 'index')
	return the_response

def owner(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	
	'''
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	'''
	loginform = AuthenticationForm()
	

	if request.user.is_authenticated():
		loggedinanon = Anon.objects.get(username=User.ojects.get(username=request.user.username))

		return render(request, 'jackdonmclovin.html', {"loggedinanon": loggedinanon, 'loginform': loginform, 'registerform': registerform, "registerterms": registerterms, 'registerterms': registerterms})

	return render(request, 'jackdonmclovin.html', {'loginform': loginform, 'registerform': registerform, "registerterms": registerterms, 'registerterms': registerterms})

def register_view(request):
	loginform = AuthenticationForm()
	login_error = "Try getting it right."
	register_error = "Don't fuck it up."
	registerform = UserCreationForm(request.POST)
	
	'''
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	'''

	if registerform.is_valid():
		new_user = registerform.save()
		register_error = "Register Successful."
		#must log in after
		user = authenticate(request, username=new_user.username, password=registerform.cleaned_data['password1'])
		if user is not None:
			login(request, user)
			Anon.objects.create(username=User.objects.get(username=new_user.username))
			Author.objects.create(username=new_user.username)
		else:
			login_error = "Not a known Combo, try using a PS4 controller."
	else:
		register_error = "Couldn't register that."
	
	return redirect('index')



def feedback(request):
	# https://stackoverflow.com/questions/31324005/django-1-8-sending-mail-using-gmail-smtp
	# email = EmailMessage('title', 'body', from_email=[], to=[jackdonmclovin@gmail.com])
	# email.send()
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	
	loginform = AuthenticationForm()
	
	contact_form = ContactForm()

	if request.user.is_authenticated:
		loggedinanon = Anon.objects.get(username=User.ojects.get(username=request.user.username))

		return render(request, 'feedback.html', {"loggedinanon": loggedinanon, 'contact_form':contact_form, 'loginform': loginform, 'registerform': registerform, "registerterms": registerterms, 'registerterms': registerterms})

	return render(request, 'feedback.html', {'contact_form':contact_form, 'loginform': loginform, 'registerform': registerform, "registerterms": registerterms, 'registerterms': registerterms})


def create_feedback(request):
	contactform = ContactForm(request.POST)
	if contactform.is_valid():
		from_email = contactform.cleaned_data['from_email']
		title = contactform.cleaned_data['title']
		message = contactform.cleaned_data['message']
		try:
			email = EmailMessage(title, message, from_email=from_email, to=['jackdonmclovin@gmail.com'])
			email.send()
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return redirect('thanks')
	return render(request, 'feedback.html', {'loginform': loginform, 'registerform': registerform, "registerterms": registerterms, 'registerterms': registerterms})

def thanks(request):
	registerform = UserCreationForm()
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	
	loginform = AuthenticationForm()

	if request.user.is_authenticated():
		loggedinanon = Anon.objects.get(username=User.ojects.get(username=request.user.username))

		return render(request, 'thanks.html', {"loggedinanon": loggedinanon, 'loginform': loginform, 'registerform': registerform, "registerterms": registerterms, 'registerterms': registerterms})

	return render(request, 'thanks.html', {'loginform': loginform, 'registerform': registerform, "registerterms": registerterms, 'registerterms': registerterms})


def about(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	with open(settings.MEDIA_ROOT + '/termsandconditions.txt') as f:
		registerterms = f.read()
	
	loginform = AuthenticationForm()
	

	if request.user.is_authenticated:
		loggedinanon = Anon.objects.get(username=User.ojects.get(username=request.user.username))

		return render(request, 'thanks.html', {"loggedinanon": loggedinanon, 'loginform': loginform, 'registerform': registerform, "registerterms": registerterms, 'registerterms': registerterms})


	return render(request, 'about.html', {'loginform': loginform, 'registerform': registerform, "registerterms": registerterms, 'registerterms': registerterms})
