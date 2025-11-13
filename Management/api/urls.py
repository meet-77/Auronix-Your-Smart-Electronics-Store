from django.urls import path
from Management.api.views import CategoryAPIView , ProductAPIView

urlpatterns = [
    path('category/', CategoryAPIView.as_view(), name='category_list_create'),
    path('product/', ProductAPIView.as_view(), name='product_list_create'),
]


