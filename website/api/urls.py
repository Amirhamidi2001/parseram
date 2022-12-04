from rest_framework.routers import DefaultRouter

from .views import *

app_name = "api"

router = DefaultRouter()
router.register('cat', CatViewSet, basename='cat')
router.register('product', ProductViewSet, basename='product')
router.register('customer', CustomerViewSet, basename='customer')
router.register('orderdetail', OrderDetailViewSet, basename='orderdetail')
router.register('order', OrderViewSet, basename='order')
urlpatterns = router.urls
