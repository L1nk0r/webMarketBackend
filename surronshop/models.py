from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
import datetime

User = get_user_model()


class Image(models.Model):
    slug = models.SlugField()
    image = models.ImageField()

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"


class ShippingDetails(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    email = models.CharField(max_length=30, verbose_name="Почта")
    phoneNumber = models.CharField(max_length=25, verbose_name="Номер телефона")
    city = models.CharField(max_length=50, verbose_name="Город")
    country = models.CharField(max_length=50, verbose_name="Страна")
    zipCode = models.CharField(max_length=20, verbose_name="Почтоый индекс")
    address = models.TextField(max_length=70, verbose_name="Адрес")


class Product(models.Model):

    article = models.IntegerField()

    title = models.CharField(
        max_length=30,
        verbose_name='Наименование'
    )

    in_stock = models.PositiveIntegerField(
        verbose_name='Количество',
        default=100,
    )

    availability = models.BooleanField(
        default=False,
        verbose_name='В наличии'
    )

    short_info = models.TextField(
        max_length=100,
        verbose_name='Короткое описание',
        null=True
    )

    info = models.TextField(
        max_length=700,
        verbose_name='Описание',
        null=False
    )

    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Цена'
    )

    draft = models.BooleanField(
        verbose_name="Черновик",
        default=False,
        null=True
    )

    img = models.ManyToManyField(
        Image,
        verbose_name='Фото товара'
    )

    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class CartProduct(models.Model):
    user = models.ForeignKey(
        'Customer',
        verbose_name='Покупатель',
        on_delete=models.CASCADE
    )

    cart = models.ForeignKey(
        'Cart',
        verbose_name='Корзина',
        on_delete=models.CASCADE,
        related_name='related_products'
    )

    product = models.ForeignKey(
        Product,
        verbose_name='Товар',
        on_delete=models.CASCADE
    )

    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Общая цена'
    )

    def __str__(self):
        return f'Cart product: {self.product.title}'

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"


class Cart(models.Model):
    owner = models.ForeignKey(
        'Customer',
        verbose_name='Владелец',
        on_delete=models.CASCADE
    )

    products = models.ManyToManyField(
        CartProduct,
        blank=True,
        related_name='related_cart'
    )

    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Общая цена'
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class Specifications(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, verbose_name='Имя товара для характеристик')

    def __str__(self):
        return f"Характеристика {self.name}"

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"


class Feedback(models.Model):
    customer_name = models.CharField(
        max_length=55,
        verbose_name='Имя заказчика'
    )

    feedback = models.ManyToManyField(Image, verbose_name="Скриншот отзыва")

    def __str__(self):
        return f"Отзыв от {self.customer_name}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Partner(models.Model):
    company_name = models.CharField(
        max_length=55,
        verbose_name="Название компании партнёра"
    )

    company_logo = models.ManyToManyField(Image, verbose_name="Лого партнёра")

    def __str__(self):
        return f"Партнёр {self.company_name}"

    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"


class Order(models.Model):
    STATUS = (
        ('Об', 'Обрабатывается'),
        ('Уп', 'Упаковывается'),
        ('От', 'Отправлен'),
        ('До', 'Доставлен'),
    )

    name = models.CharField(max_length=30, verbose_name="Имя")
    email = models.CharField(max_length=30, verbose_name="Почта")
    phoneNumber = models.CharField(max_length=25, verbose_name="Номер телефона")
    city = models.CharField(max_length=50, verbose_name="Город")
    country = models.CharField(max_length=50, verbose_name="Страна")
    zipCode = models.CharField(max_length=20, verbose_name="Почтоый индекс")
    comment = models.TextField(max_length=255, verbose_name="Комментарий", default="")
    status = models.CharField(max_length=50, verbose_name="Статус заказа", choices=STATUS, default='Об')

    products = models.ManyToManyField(Product, verbose_name='Товары заказа')

    date = models.DateField(verbose_name='Дата заказа')

    total_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Общая цена'
    )

    address = models.TextField(
        max_length=255,
        verbose_name='Адрес'
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class HandMadeOrder(models.Model):
    STATUS = (
        ('Об', 'Обрабатывается'),
        ('Уп', 'Упаковывается'),
        ('От', 'Отправлен'),
        ('До', 'Доставлен'),
    )

    date = models.DateField(verbose_name="Дата заказа", default=datetime.date.today)

    name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )

    address = models.TextField(
        max_length=300,
        verbose_name="Адрес"
    )

    email = models.CharField(
        max_length=50,
        verbose_name="Почта"
    )

    phoneNumber = models.CharField(
        max_length=30,
        verbose_name="Номер телефона"
    )

    products = models.TextField(
        max_length=1000,
        verbose_name="Товары"
    )

    total_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Общая цена'
    )

    status = models.CharField(max_length=50, verbose_name="Статус заказа", choices=STATUS, default='Об')

    def str(self):
        return str(self.id)

    class Meta:
        verbose_name = "Заказ в ручную"
        verbose_name_plural = "Заказы в ручную"


class Customer(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=[('user', 'customer'),
                 ('super', 'superuser'),
                 ('ship', 'superuser')],
        verbose_name='Роль',
        default='user'
    )

    orders = models.ManyToManyField(HandMadeOrder, verbose_name="Заказы")

    phone = models.CharField(
        max_length=20,
        verbose_name='Номер телефона'
    )

    address = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )

    def __str__(self):
        return f"Покупатель {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
