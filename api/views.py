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
from rest_framework.decorators import api_view
from django.http import HttpResponseBadRequest

load_dotenv()

# get all businesses
@api_view(['GET'])
def yelp_search(request=None):
    print(request.query_params)
    term =  request.query_params.get('term', None)
    location = request.query_params.get('location', None)
    token = os.environ.get('API_KEY')

    if term is None:
        return HttpResponseBadRequest()


    YELP_SEARCH_ENDPOINT = "https://api.yelp.com/v3/businesses/search"
    headers = {'Authorization': 'Bearer '  + token}
    params = { 'term' :term, 'location' :location}

    r = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params)

    r=r.json()
    print(r)
    data = r.get('businesses')
    

    return JsonResponse(data, safe=False)

# get one businesses
@api_view(["GET"])
def business_detail(request, business_id):
    # business_id =  request.query_params["business_id"]
    # business_id = request.get("business_id")
   
    
    token = os.environ.get('API_KEY')
    YELP_DETAIL_ENDPOINT = "https://api.yelp.com/v3/businesses/{}".format(business_id)
    headers = {"Authorization": "Bearer " + token}

    r = requests.get(YELP_DETAIL_ENDPOINT, headers=headers)
    business_info=r.json()
    # business_info=r.get('name')
  

    return JsonResponse(business_info)

# ----------------------add favoris----------------------

# save result once client add a business as favoris

# ----------------------add favoris----------------------

class FavorisViewSet(viewsets.ModelViewSet):
    queryset = Favoris.objects.all()
    serializer_class = FavorisSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

