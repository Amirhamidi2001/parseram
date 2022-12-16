from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    """
    This class is for specifying product categories
    """
    title = models.CharField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey(
        'self',
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='child'
    )

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Product(models.Model):
    """
    This class is for registering products
    """
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True)
    content = models.CharField(max_length=255)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.title


CITY_CHOICES = (
    ('Tehran', 'Tehran'),
    ('Shiraz', 'Shiraz'),
    ('Tabriz', 'Tabriz'),
    ('Mashhad', 'Mashhad'),
    ('Esfehan', 'Esfehan'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class Customer(models.Model):
    """
    This class is for storing customer information
    """
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    age = models.IntegerField(
        validators=[MinValueValidator(14), MaxValueValidator(100)]
    )
    city = models.CharField(choices=CITY_CHOICES, max_length=10)
    address = models.TextField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)

    def __str__(self):
        return self.name


class OrderDetail(models.Model):
    """
    This class is for ordering
    """
    order = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_item_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    """
    This class is for finalizing the order
    """
    user = models.ForeignKey("Customer", on_delete=models.CASCADE)
    items = models.ManyToManyField("OrderDetail")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
