from api.models import Favoris
from django.shortcuts import render
from .serializers import FavorisSerializer, UserSerializer
from rest_framework import viewsets
import requests
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

load_dotenv()



def yelp_search(request=None):
    token = os.environ.get('API_KEY')

    # token = "Z1I-d_WXmtZ0e8Lfz5nGwW9K1rjGcIMbG5VU-E9nrVm8pVZF3cs-3aJgBbEcGd6GSNMoIXiA_80yOkhCVKTr_AQe8oKDDwMAY2uvk_yuS7R_c5VH_D7Kfn1XnoEDYXYx"
    YELP_SEARCH_ENDPOINT = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization": "Bearer " + token}
    params = {'term': 'black hair salon', 'location': 'houston'}

    r = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params)

    r=r.json()
    data = r.get('businesses')
    

    return JsonResponse(data, safe=False)


def business_detail(request, business_id):
    # business_id = "oQRH4El0rM5MCoFxLdtiMA"
    # token = "Z1I-d_WXmtZ0e8Lfz5nGwW9K1rjGcIMbG5VU-E9nrVm8pVZF3cs-3aJgBbEcGd6GSNMoIXiA_80yOkhCVKTr_AQe8oKDDwMAY2uvk_yuS7R_c5VH_D7Kfn1XnoEDYXYx"
    token = os.environ.get('API_KEY')
    YELP_DETAIL_ENDPOINT = "https://api.yelp.com/v3/businesses/{}".format(business_id)
    headers = {"Authorization": "Bearer " + token}
    # params = {'term': 'black hair salon', 'location': 'houston'}

    r = requests.get(YELP_DETAIL_ENDPOINT, headers=headers)
    business_info=r.json()
    # business_info=r.get('name')
  

    return JsonResponse(business_info)

class FavorisViewSet(viewsets.ModelViewSet):
    queryset = Favoris.objects.all()
    serializer_class = FavorisSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

