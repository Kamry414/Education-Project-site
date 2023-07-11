from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Category, Product, Sale, Banner, Tag
from .serializers import CategorySerializer, ProductSerializer, SaleSerializer, BannerSerializer, TagSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ProductReviewCreateView(APIView):
    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        author = request.data.get('author')
        email = request.data.get('email')
        text = request.data.get('text')
        rate = request.data.get('rate')
        date = request.data.get('date')

        # Create the review object and associate it with the product
        review = {
            'author': author,
            'email': email,
            'text': text,
            'rate': rate,
            'date': date,
        }
        product.reviews.append(review)
        product.save()

        return Response({'message': 'Review added successfully'}, status=201)



class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PopularProductList(generics.ListAPIView):
    queryset = Product.objects.filter(is_popular=True)
    serializer_class = ProductSerializer


class LimitedProductList(generics.ListAPIView):
    queryset = Product.objects.filter(is_limited=True)
    serializer_class = ProductSerializer


class SaleList(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer



class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
