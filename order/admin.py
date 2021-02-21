from django.contrib import admin
from order.models import ShopCardModel
# Register your models here.


@admin.register(ShopCardModel)
class ShopCardAdmin(admin.ModelAdmin):
    search_fields = ("product", 'desc')
    list_display = ("product",)