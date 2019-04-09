from django.urls import path
from .views import UserCreateAPIView
from rest_framework_jwt.views import obtain_jwt_token
from api.views import (UserCreateAPIView,UserUpdateView,ItemListView,ItemDetailView,CheckOutView,OrderHistoryView,OrderControlAPIView,OrderDetailView,CartDeleteView,CartListView)

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('userupdate/', UserUpdateView.as_view(), name='userupdate'),
    path('list/', ItemListView.as_view(), name='api-list'),
    path('details/<int:item_id>', ItemDetailView.as_view(), name='api-detail'),
    path('checkout/<int:order_id>', CheckOutView.as_view(), name='api-checkout'),
    path('cart/<int:id>', CartListView.as_view(), name='api-cart'),
    path('deletecart/<int:cart_id>', CartDeleteView.as_view(), name='api-deletecart'),
    path('order/', OrderDetailView.as_view(), name='api-deletecart'),
    path('history/', OrderHistoryView.as_view(), name='api-history'),
    path('ctrl_order/<int:item_id>', OrderControlAPIView.as_view(), name='api-order_list'),
    
]