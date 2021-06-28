from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',]


class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True) # для ManyToMany many=True

    class Meta:
        model = Customer
        fields = '__all__'


class CreateProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True) # для ManyToMany many=True

    class Meta:
        model = Producer
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    category = serializers.CharField(source='get_category_display')

    class Meta:
        model = Order
        fields = '__all__'


class CreateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    producer = ProducerSerializer()

    class Meta:
        model = Offer
        fields = '__all__'


class CreateContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    offer = OfferSerializer()
    order = OrderSerializer()

    class Meta:
        model = Contract
        fields = '__all__'


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    producer = ProducerSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    contract = ContractSerializer()
    author = UserSerializer()
    customer = CustomerSerializer()
    producer = ProducerSerializer()
    rating = serializers.CharField(source='get_rating_display')

    class Meta:
        model = Review
        fields = '__all__'


class CreateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Tag
        fields = '__all__'


