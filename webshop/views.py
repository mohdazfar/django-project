from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import products, vat_info
from . serializers import productSerializer
from django.db.models import Q


def index(request):
    '''
    Search for the item_id and return the data for that
    specific item_id
    :param request:
    :return: serialized data in JSON format
    '''
    query = request.GET.get('query')
    if query:
        response_url = 'products?item_id={}&format=json'.format(query)
        return HttpResponseRedirect(response_url)
    product_list = products.objects.all()
    serializer = productSerializer(product_list, many=True)
    return render(request, 'index.html', {'data': serializer.data})


def post_form(request):
    '''
    Redirects to form for generating products
    :param request:
    :return:
    '''
    return render(request, 'addProducts.html')


def post_form_data(request):
    '''
    GET the data from input fields from the form
    and save it to database
    :param request: request django parameter for a request
    :return:  Unique identifier and item_id for the newly created cart
    '''
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        manufacturing_country = request.POST.get('manufacturing_country')
        json_format_data = {
            'item_id': item_id,
            'item_name': item_name,
            'item_price' : item_price,
            'manufacturing_country': manufacturing_country
        }
        serializer = productSerializer(data=json_format_data)

        if serializer.is_valid():
            serializer.save()
            print(serializer)
            last_product = products.objects.last()
            temp_serializer = productSerializer(last_product)
            temp_serializer =  temp_serializer.data
            unique_identifier = temp_serializer['id']
            itemID = temp_serializer['item_id']
            context = [{'item_id': itemID, 'id':unique_identifier}]
            return render(request, 'post_data_response.html', {'context': context})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productList(APIView):

    def get(self, request):
        '''
        GET request is handled here.
        url_1 = 'http://localhost:8000/products --> return cart info of all the products
        url_2 = 'http://localhost:8000/products?item_id={ITEM_ID} --> return cart info of ITEM_ID

        :param request: request django parameter for a request
        :return: serialized data in a proper JSON format
        '''
        product_list = products.objects.all()
        serializer = productSerializer(product_list, many=True)
        query = self.request.GET.get("id") or self.request.GET.get("item_id")
        if query:
            product_list = product_list.filter(
                Q(item_id=query)|
                Q(id=query)).distinct()
            serializer = productSerializer(product_list, many=True)
        return Response(serializer.data)



    def post(self, request):
        '''
        POST request is handle here
        Can use POSTMAN
        url = 'http://localhost:8000/products'
        And in the body give the JSON data like the following
        {
        "item_id" : "101526477",
        "item_price" : 99.00,
        "item_name": "GARMIN VIVOFIT JR LAVA",
        "manufacturing_country": "9"
        }
        :param request: request django parameter for a request
        :return: Response is unique identifier and item_id for the newly created cart
        '''
        serializer = productSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            last_product = products.objects.last()
            temp_serializer = productSerializer(last_product)
            temp_serializer =  temp_serializer.data
            unique_identifier = temp_serializer['id']
            itemID = temp_serializer['item_id']
            response = 'Unique Identifier (id): {}, ' \
                       'item_id: {}'.format(unique_identifier,itemID)
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

