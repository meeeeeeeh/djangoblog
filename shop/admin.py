
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Product, CategoryProduct, Review, Basket, ProductInBasket, Order

admin.site.register(Product)


class CategoryProductMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ('name', 'parent', 'tree_id', 'level')
    fields = ('name', 'parent')


admin.site.register(CategoryProduct, CategoryProductMPTTModelAdmin)
admin.site.register(Review)
admin.site.register(Basket)
admin.site.register(ProductInBasket)
admin.site.register(Order)
