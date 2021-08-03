from django.urls import path
from api import views


urlpatterns = [
    path('api/',  views.yelp_search, name='yelp_search'),
    path('<str:business_id>/', views.business_detail, name='business_detail')

]