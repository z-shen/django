# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django import template
#from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.utils import timezone

from restaurants.models import Restaurant,Food,Comment

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

#def menu(request):
#	food1 = { 'name':'番茄炒蛋','price':60,'comment':'好吃','is_spicy' :False }
#	food2 = {'name':'蒜泥白肉','price':120,'comment':'好吃','is_spicy':False } 
#	foods=[food1,food2]
#	return render_to_response('menu.html',locals())


def menu(request,id):
	if id:
		restaurant = Restaurant.objects.get(id=id)
		return render_to_response('menu.html',locals())
	else:
		return HttpResponseRedirect("/restaurants_list/")
def meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k,v in values:
		html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k,v))
	return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('restaurants_list.html',locals()) 

def comment(request,id):
	if id:
		r = Restaurant.objects.get(id=id)
	else:	
		return HttpResponseRedirect("/restaurants_list/")
	if request.POST:
		visitor = request.POST['visitor']
		content = request.POST['content']
		email = request.POST['email']
		date_time = timezone.localtime(timezone.now())	
		Comment.objects.create(
			visitor = visitor,
			email = email,
			date_time = date_time,
			content = content,
			restaurant = r )
	return render_to_response('comments.html',locals())
