from django.urls import path
from categories.views import CategoryListView, CategoryDetailView, CategoryImageViewSet


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:category_id>/images/', CategoryImageViewSet.as_view(), name='category-images'),
]
