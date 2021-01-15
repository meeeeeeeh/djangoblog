from django.db import models
from decimal import Decimal
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models import Avg
from django.utils import timezone


class CategoryProduct(MPTTModel):
    class Meta:
        db_table = 'category_product'
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=35, verbose_name='Категория')
    parent = TreeForeignKey('self', null=True, blank=True,
                            on_delete=models.CASCADE, related_name='children', verbose_name="Родительская категория")

    def str(self):
        return f'{self.name}'

    class MPTTMeta:
        order_insertion_by = ['name']


class Product(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(max_length=200, verbose_name='Описание')
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=Decimal("0.00"),
                               verbose_name='Цена')
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Категория', blank=True,
                                 null=True)

    cover = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'

    @property
    def rating(self):
        rating = Review.objects.filter(product=self.pk).aggregate(Avg('value'))
        return rating['value__avg']


class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар', related_name='review',
                                blank=True, null=True)
    text = models.TextField(max_length=200, verbose_name='Отзыв', blank=True, null=True)
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    value = models.IntegerField(
        choices=RATING_CHOICES, verbose_name='value', default=5
    )

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'{self.text}'


class Basket(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

    @property
    def total_cost(self):
        products_in_basket = ProductInBasket.objects.filter(basket=self)
        total_cost = 0
        for product in products_in_basket:
            total_cost += product.products.cost * product.product_count
        return total_cost


class ProductInBasket(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, blank=True, null=True)
    product_count = models.IntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f'{self.products.name}'


class Order(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateField(auto_now_add=timezone.now)
    STATUS_CHOICES = (
        ('Обработка заказа', 'Обработка заказа'),
        ('Доставка', 'Доставка'),
        ('Получен', 'Получен'),

    )
    status = models.TextField(max_length=30, choices=STATUS_CHOICES)


class Favorites(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)







