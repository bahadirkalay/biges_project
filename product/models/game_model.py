from django.db import models
from autoslug import AutoSlugField
import datetime
from product.models import CategoryModel
# Create your models here.

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class GameModel(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False verbose_name="Oyunun Adı")
    year = models.IntegerField(('year'), choices=year_choices, default=current_year , verbose_name="Yıl")
    category = models.ManyToManyField(CategoryModel , verbose_name="Kategori Adı")
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        verbose_name = 'Oyun'
        verbose_name_plural = 'Oyunlar'
        db_table = 'game'
    
    def __str__(self):
        return self.name
    


