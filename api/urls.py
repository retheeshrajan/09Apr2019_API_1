from django.urls import path
from .views import UserCreateAPIView
from rest_framework_jwt.views import obtain_jwt_token
from api.views import (ItemListView,ItemDetailView,CartListView,CartCreateAPIView,UserUpdateView,CartListView
    ,OrderUpdateView,ItemCreateAPIView,CartUpdateView,OrderControlAPIView)

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('userupdate/<int:user_id>', UserUpdateView.as_view(), name='userupdate'),
    path('list/', ItemListView.as_view(), name='api-list'),
    path('details/<int:item_id>', ItemDetailView.as_view(), name='api-detail'),
    path('update_order/<int:order_id>', OrderUpdateView.as_view(), name='api-updateorder'),
    path('cart/', CartListView.as_view(), name='api-cart'),
    path('addcart/', CartCreateAPIView.as_view(), name='api-addcart'),
    path('update_item/<int:item_id>', CartUpdateView.as_view(), name='api-updateitem'),
    path('additem/', ItemCreateAPIView.as_view(), name='api-additem'),
    path('ctrl_order/<int:item_id>', OrderControlAPIView.as_view(), name='api-ctrl-order'),
   
]