# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django import template
#from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def here(request):
	return HttpResponse('Mom, 我在這')

def add(request,a,b):
	a = int(a)
        b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	
#	t = get_template('math.html')
#	c = template.Context({'s':s,'d':d,'p':p,'q':q})
 	return render_to_response('math.html',locals())

def menu(request):
	food1 = { 'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy' :False }
	food2 = {'name':'蒜泥白肉','price':120,'comment':'好吃','is_spicy':False } 
	foods=[food1,food2]
	return render_to_response('menu.html',locals())


def welcome(request):
	if 'user_name' in request.GET and request.GET['user_name'] != "":
		return HttpResponse('Welcome!~'+request.GET['user_name'])	
	else:
		return render_to_response('welcome.html',locals())

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')
	
	username=request.POST.get('username','')
	password=request.POST.get('password','')

	user = auth.authenticate(username=username,password=password)
	
	if user is not None and user.is_active:
		auth.login(request,user)
		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('login.html',RequestContext(request, locals()))
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index')

def index(request):
	return render_to_response('index.html',RequestContext(request, locals()))

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect('/accounts/login/')
	else:
		form = UserCreationForm()
	return render_to_response('register.html',RequestContext(request,locals()))
		

