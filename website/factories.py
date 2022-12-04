import factory
from factory.django import DjangoModelFactory

from .models import Customer

class CustomerFactory(DjangoModelFactory):

    class Meta:
        model = Customer

    name = factory.Faker("first_name")
    family = factory.Faker("last_name")
    age = factory.random.randint(1, 100)
    city = factory.Faker("")
    address = factory.Faker("address")
    gender = factory.Faker("")
