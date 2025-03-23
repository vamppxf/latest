from django.urls import path
from products.views import ProductViewSet, ReviewViewSet, FavoriteProductViewSet, CartViewSet, TagList, ProductImageViewSet

urlpatterns = [
    path('products/', ProductViewSet.as_view(), name="products"),
    path('products/<int:pk>', ProductViewSet.as_view(), name='product'),
    path('products/<int:product_id>/images/', ProductImageViewSet.as_view(), name="product-images"),
    path('products/<int:product_id>/images/<int:pk>', ProductImageViewSet.as_view(), name="product-image"),
    path('reviews/', ReviewViewSet.as_view(), name="reviews"),
    path('favorite_products/', FavoriteProductViewSet.as_view(), name='favorite_products'),
    path('favorite_products/<int:pk>/', FavoriteProductViewSet.as_view(), name='favorite_product'),
    path('cart/', CartViewSet.as_view(), name='cart'),
    path('tags/', TagList.as_view(), name='tags')
]