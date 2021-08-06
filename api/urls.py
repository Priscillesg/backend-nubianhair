from django.urls import path, include
from .views import yelp_search, business_detail, FavorisViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('favoris', FavorisViewSet, basename='favoris')
router.register('users', UserViewSet)

urlpatterns = [
    path('api_list/', yelp_search),
    path('api_list/<business_id>', business_detail),
    path('api/', include(router.urls)),

]