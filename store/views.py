from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        qset = Product.objects.select_related("collection").all()
        serializer = ProductSerializer(
            qset, many=True, context={'request': request})

        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        
        return Response("ok")


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)

    return Response(serializer.data)


@api_view()
def collection_list(request):
    qset = Collection.objects.all()
    serializer = CollectionSerializer(
        qset, many=True, context={'request': request})

    return Response(serializer.data)


@api_view()
def collection_detail(request, id):
    collection = get_object_or_404(Collection, pk=id)
    serializer = CollectionSerializer(collection)
    
    return Response(serializer.data)
