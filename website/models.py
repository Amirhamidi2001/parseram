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
        on_delete=models.CASCADE,
        related_name='child'
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    This class is for registering products
    """
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True)
    content = models.CharField(max_length=255)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)

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
    o = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"


class Order(models.Model):
    """
    This class is for finalizing the order
    """
    user = models.ForeignKey("Customer", on_delete=models.CASCADE)
    date = models.DateField(null=True)
    totalprice = models.IntegerField(null=True)

    def __str__(self):
        return self.user.name
