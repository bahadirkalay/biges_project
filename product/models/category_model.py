from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length=40, blank=False, null=False)
    slug = AutoSlugField(populate_from='title', unique = True)
    

    class Meta:
        db_table = 'category'
        verbose_name_plural ='Kategoriler'
        verbose_name ='Kategori'

    def __str__(self):
        return self.title
    