from api.models import Favoris
from django.shortcuts import render
from .serializers import FavorisSerializer, UserSerializer
from rest_framework import serializers, viewsets, status
import requests
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from django.http import HttpResponseBadRequest, HttpResponse
from .models import Favoris
from rest_framework.response import Response



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
@api_view(["GET"])
def favourites_list(request, slug):
  
    try:
        favoris = Favoris.objects.get(slug=slug)
    except Favoris.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FavorisSerializer(favoris)
        return Response(serializer.data)

# @api_view(["POST",])
# def create_favourites(request):
#         serializer = FavorisSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------------------
@api_view(["GET"])
def favouritesList(request):
    favourites = Favoris.objects.all()
    serializer = FavorisSerializer(favourites, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def createList(request):
    serializer = FavorisSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteFavourite(request, pk):
    favourite = Favoris.objects.get(id=pk)
    favourite.delete()
    # return Response(status=status.HTTP_204_NO_CONTENT)
    return Response("Item successfully delete!")


# class FavorisViewSet(viewsets.ModelViewSet):
#     queryset = Favoris.objects.all()
#     serializer_class = FavorisSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class Locate_API(APIView):    # API view of the saved results in the database

#     def get(self,request):
#         results = Favoris.objects.all()
#         serializer = FavorisSerializer(results, many = True)

#         return Response(serializer.data)
