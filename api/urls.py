from django.urls import path
from .views import UserCreateAPIView
from rest_framework_jwt.views import obtain_jwt_token
from api.views import (ItemListView,ItemDetailView,CartListView,CartCreateAPIView,UserUpdateView,CartListView,OrderCreateAPIView,OrderUpdateView,OrderDetailView)

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('userupdate/<int:user_id>', UserUpdateView.as_view(), name='userupdate'),
    path('list/', ItemListView.as_view(), name='api-list'),
    path('details/<int:item_id>', ItemDetailView.as_view(), name='api-detail'),
    path('add_order/', OrderCreateAPIView.as_view(), name='api-addorder'),
    path('details_order/<int:order_id>', OrderDetailView.as_view(), name='api-detailorder'),
    path('update_order/<int:order_id>', OrderUpdateView.as_view(), name='api-updateorder'),
    path('cart/', CartListView.as_view(), name='api-cart'),
    path('addcart/', CartCreateAPIView.as_view(), name='api-addcart'),
   
]