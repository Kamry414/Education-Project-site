from django.urls import path
from product import views


urlpatterns = [

    path('product/<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:id>/review/', views.ProductReviewCreateView.as_view(), name='product-review-create'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('catalog/', views.ProductList.as_view(), name='catalog'),
    path('products/popular/', views.PopularProductList.as_view(), name='popular-products'),
    path('products/limited/', views.LimitedProductList.as_view(), name='limited-products'),
    path('sales/', views.SaleList.as_view(), name='sales'),
    path('banners/', views.BannerList.as_view(), name='banners'),
    path('tags/', views.TagListView.as_view(), name='tags'),
]
