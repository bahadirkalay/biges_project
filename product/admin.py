from django.contrib import admin
from product.models import GameModel, CategoryModel
# Register your models here.

@admin.register(GameModel)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ("name", 'desc')
    list_display = ("name", 'year',)

@admin.register(CategoryModel)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ("title", 'desc')
    list_display = ("title",)

