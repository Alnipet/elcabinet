from django.contrib import admin
from django.urls import path, include

from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = (
    path('customers/<int:pk>', CustomerRetrieveView.as_view()),
    path('customers/update/<int:pk>', CustomerUpdateView.as_view()),
    path('customers/new', CustomerCreateView.as_view()),
    path('customers/all', CustomerListView.as_view()),

    path('producers/<int:pk>', ProducerRetrieveView.as_view()),
    path('producers/update/<int:pk>', ProducerUpdateView.as_view()),
    path('producers/new', ProducerCreateView.as_view()),
    path('producers/all', ProducerListView.as_view()),

    path('orders/<int:pk>', OrderRetrieveView.as_view()),
    path('orders/update/<int:pk>', OrderUpdateView.as_view()),
    path('orders/new', OrderCreateView.as_view()),
    path('orders/all', OrderListView.as_view()),

    path('offers/<int:pk>', OfferRetrieveView.as_view()),
    path('offers/update/<int:pk>', OfferUpdateView.as_view()),
    path('offers/new', OfferCreateView.as_view()),
    path('offers/all', OfferListView.as_view()),

    path('contracts/<int:pk>', ContractRetrieveView.as_view()),
    path('contracts/update/<int:pk>', ContractUpdateView.as_view()),
    path('contracts/new', ContractCreateView.as_view()),
    path('contracts/all', ContractListView.as_view()),

    path('messages/<int:pk>', MessageRetrieveView.as_view()),
    path('messages/update/<int:pk>', MessageUpdateView.as_view()),
    path('messages/new', MessageCreateView.as_view()),
    path('messages/all', MessageListView.as_view()),

    path('reviews/<int:pk>', ReviewRetrieveView.as_view()),
    path('reviews/update/<int:pk>', ReviewUpdateView.as_view()),
    path('reviews/new', ReviewCreateView.as_view()),
    path('reviews/all', ReviewListView.as_view()),

    path('tags/<int:pk>', TagRetrieveView.as_view()),
    path('tags/update/<int:pk>', TagUpdateView.as_view()),
    path('tags/new', TagCreateView.as_view()),
    path('tags/all', TagListView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
)



