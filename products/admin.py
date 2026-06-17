from django.contrib import admin
from .models import Product, Category, Tag

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category', 'tags')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Tag)