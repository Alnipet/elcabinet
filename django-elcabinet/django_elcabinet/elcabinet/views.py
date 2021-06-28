from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .models import *
from .serializers import *

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsCustomer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# Customer
class CustomerRetrieveView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateView(generics.UpdateAPIView):  # нет метода GET, можно использовать class RetrieveUpdateAPIView
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# Producer
class ProducerRetrieveView(generics.RetrieveAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ProducerUpdateView(generics.UpdateAPIView):  # нет метода GET, можно использовать class RetrieveUpdateAPIView
    queryset = Producer.objects.all()
    serializer_class = CreateProducerSerializer


class ProducerCreateView(generics.CreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = CreateProducerSerializer


class ProducerListView(generics.ListAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


# Order
class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):  # нет метода GET, можно использовать class RetrieveUpdateAPIView
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):  # Фильтр
        queryset = Order.objects.all()

        params = self.request.query_params
        category = params.get('category', None)
        budget_order = params.get('budget_order', None)
        customer = params.get('customer', None)

        if category:
            queryset = queryset.filter(category=category)

        if budget_order:
            queryset = queryset.filter(budget_order__lte=budget_order)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        return queryset


# Offer
class OfferRetrieveView(generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferUpdateView(generics.UpdateAPIView):  # нет метода GET, можно использовать class RetrieveUpdateAPIView
    queryset = Offer.objects.all()
    serializer_class = CreateOfferSerializer


class OfferCreateView(generics.CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = CreateOfferSerializer


class OfferListView(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


# Contract
class ContractRetrieveView(generics.RetrieveAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractUpdateView(generics.UpdateAPIView):  # нет метода GET, можно использовать class RetrieveUpdateAPIView
    queryset = Contract.objects.all()
    serializer_class = CreateContractSerializer


class ContractCreateView(generics.CreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = CreateContractSerializer


class ContractListView(generics.ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


# Message
class MessageRetrieveView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdateView(generics.UpdateAPIView):  # нет метода GET, можно использовать class RetrieveUpdateAPIView
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# Review
class ReviewRetrieveView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewUpdateView(generics.UpdateAPIView):  # нет метода GET, можно использовать class RetrieveUpdateAPIView
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# Tag
class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(generics.UpdateAPIView):  # нет метода GET, можно использовать class RetrieveUpdateAPIView
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer


class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
