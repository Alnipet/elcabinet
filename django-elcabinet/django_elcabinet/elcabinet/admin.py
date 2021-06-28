from django.contrib import admin
from . import models


class CustomerAdmin(admin.ModelAdmin):
    pass


class ProducerAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    fields = ('customer',
              'title',
              ('city_order', 'category'),
              ('placement_date', 'last_modified_date'),
              ('expiration_date', 'budget_order'),
              'requirement',
              'description',
              'file_order')
    readonly_fields = ('placement_date', 'last_modified_date')


class OfferAdmin(admin.ModelAdmin):
    fields = ('title',
              'producer', 'order',
              'price_offer',
              ('placement_date', 'last_modified_date'),
              'description',
              'file_offer')
    readonly_fields = ('placement_date', 'last_modified_date')


class ContractAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Producer, ProducerAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Offer, OfferAdmin)
admin.site.register(models.Contract, ContractAdmin)
admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.Review, ReviewAdmin)