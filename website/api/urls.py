from rest_framework.routers import DefaultRouter

from .views import *

app_name = "api"

router = DefaultRouter()
router.register('cat', CatViewSet, basename='cat')
router.register('product', ProductViewSet, basename='product')
urlpatterns = router.urls
