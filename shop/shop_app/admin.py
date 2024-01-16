from django.contrib import admin
from .models import Category, Product


class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
    list_display_links = ['slug', 'name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'update',
                    'image', 'description']
    list_filter = ['available', 'price', 'update']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10
