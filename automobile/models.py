from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "категория авто"
        verbose_name_plural = "категории авто"

    def __str__(self):
        return self.name


class Auto(models.Model):
    brand = models.CharField(max_length=30)
    produced_year = models.PositiveSmallIntegerField()
    price = models.FloatField(default=0)
    info = models.TextField(null=False, default='')
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="autos")

    class Meta:
        verbose_name = "автомобиль"
        verbose_name_plural = "автомобили"

    def __str__(self):
        return self.brand, self.produced_year

