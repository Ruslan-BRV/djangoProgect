from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=100)
    price = models.FloatField(verbose_name="Цена")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name