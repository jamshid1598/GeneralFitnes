from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import (
    Category,
    Product,
    ProductImage,
)

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display       = ()
    list_display_links = ()
    list_editable      = ()
    search_fields      = ()
    ordering           = ()

    prepopulated_fields = {'slug' : ('name',)}

    fieldsets = (
        ('Category Info', {
            "fields": (
                
            ),
        }),
    )    
admin.site.register(Category, CategoryAdmin)



class ProductImageAdmin(admin.TabularInline):
    model   = ProductImage
    extra   = 1
    max_num = 4

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin,]

    list_display       = ()
    list_display_links = ()
    list_editable      = ()
    search_fields      = ()
    ordering           = ()

    prepopulated_fields = {'slug' : ('name',)}

    fieldsets = (
        ('Proruct Info', {
            "fields": (
                
            ),
        }),
    )    
admin.site.register(Product, ProductAdmin)