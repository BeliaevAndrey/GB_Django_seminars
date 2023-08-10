from django.contrib import admin
from .models import Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    ordering = ('name', 'email', 'address')
    list_filter = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ['reg_date', 'reg_date']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'email', 'phone'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'fields': ['address', 'reg_date']
            },
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    ordering = ('name', 'price', 'amount')
    list_filter = ('name', 'price', 'amount')
    search_fields = ('name', 'price', 'description')

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'price', 'amount'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'fields': ['description', 'add_date', 'p_image']
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    ordering = ('customer', 'product', 'total_price')
    list_filter = ('customer', 'product', 'order_date')
    search_fields = ('customer', 'product', 'order_date')
    readonly_fields = ('order_date', 'total_price')


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
