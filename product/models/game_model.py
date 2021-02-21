from django.db import models
from autoslug import AutoSlugField
import datetime
from product.models import CategoryModel
from django.contrib.auth.models import User
# Create your models here.

class GameModel(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE , null=True)
    name = models.CharField(max_length=80, blank=False, null=False ,verbose_name="Oyunun Adı")
    year = models.IntegerField(verbose_name="Yıl")
    category = models.ManyToManyField(CategoryModel , verbose_name="Kategori Adı")
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        verbose_name = 'Oyun'
        verbose_name_plural = 'Oyunlar'
        db_table = 'game'
    
    def __str__(self):
        return self.name
    


