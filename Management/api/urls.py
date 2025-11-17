from django.urls import path
from Management.api.views import CategoryAPIView , ProductAPIView , CategorydetalisAPIView , ProductdetailsAPIView , OrderAPIView , OrderdetailsAPIView

urlpatterns = [
    path('category/', CategoryAPIView.as_view(), name='category_list_create'),
    path('category/<int:pk>/', CategorydetalisAPIView.as_view(), name='category_detail'),
    
    path('product/', ProductAPIView.as_view(), name='product_list_create'),
    path('product/<int:pk>/' , ProductdetailsAPIView.as_view(), name='product_details' ),
    
    path('order/',OrderAPIView.as_view() , name='order_list_create'),
    path('order/<int:pk>/',OrderdetailsAPIView.as_view() , name='order_details'),
]


