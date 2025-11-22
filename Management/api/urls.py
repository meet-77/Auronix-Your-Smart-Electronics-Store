from django.urls import path
from Management.api.views import CategoryAPIView , ProductAPIView , CategorydetalisAPIView , ProductdetailsAPIView , OrderAPIView , OrderdetailsAPIView , UserViewSet , RegisterAPI , LoginAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='api_register'),
    path('login/', LoginAPI.as_view(), name='api_login'),
    path('category/', CategoryAPIView.as_view(), name='category_list_create'),
    path('category/<int:id>/', CategorydetalisAPIView.as_view(), name='category_detail'),
    
    path('product/', ProductAPIView.as_view(), name='product_list_create'),
    path('product/<int:id>/' , ProductdetailsAPIView.as_view(), name='product_details' ),
    
    path('order/',OrderAPIView.as_view() , name='order_list_create'),
    path('order/<int:id>/',OrderdetailsAPIView.as_view() , name='order_details'),
]


urlpatterns += router.urls