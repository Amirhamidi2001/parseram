from django.core.management.base import BaseCommand
from faker import Faker

from ...models import *


CITY_CHOICES = (
    ('Tehran'),
    ('Shiraz'),
    ('Tabriz'),
    ('Mashhad'),
    ('Esfehan'),
)


GENDER_CHOICES = (
    ('Male'),
    ('Female'),
)


class Command(BaseCommand):
    help = 'inserting dummy data'

    def __init__(self, *args, **kwargs) -> None:
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        for _ in range(50):
            Product.objects.create(
                title = self.fake.word(),
                content = self.fake.text(100),
                description = self.fake.text(),
                price = self.fake.pyint(),
                category = self.fake.random_element(Category.objects.filter(parent = True)),
            )

        for _ in range(1000):
            customer = Customer.objects.create(
                name = self.fake.first_name(),
                family = self.fake.last_name(),
                age = self.fake.random_int(14, 100),
                city = self.fake.random_element(CITY_CHOICES),
                address = self.fake.address(),
                gender = self.fake.random_element(GENDER_CHOICES)
            )

            for _ in range(500):
                OrderDetail.objects.create(
                    user = customer,
                    product = self.fake.random_element(Product.objects.all()),
                    quantity = self.fake.random_int(1, 3),
                    date = self.fake.date_this_month(),
                )
