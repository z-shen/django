from django.contrib import admin
from restaurants.models import Restaurant,Food,Comment
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name','phone_number','address')
	search_fields = ('name',)
class FoodAdmin(admin.ModelAdmin):
	list_display = ('name','restaurant','price','is_spicy')
	list_filter = ('is_spicy','restaurant')
	search_fields = ('name','price','restaurant__name')
	ordering = ('price',)
	fields = ('price','is_spicy','restaurant')
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(Comment)
