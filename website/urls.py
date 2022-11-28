from django.urls import path, include

from .views import *

app_name = "website"

urlpatterns = [
    path("", CatView.as_view(), name='cat-view'),
    path("product/", ProductView.as_view(), name='cat-view'),
    path("api/", include("website.api.urls"))
]
