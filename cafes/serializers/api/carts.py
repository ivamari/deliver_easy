from django.contrib.auth import get_user_model
from rest_framework import serializers

from cafes.models.carts import Cart, CartProduct
from cafes.models.products import Product
from cafes.serializers.nested.products import ProductShortSerializer
from common.serializers.mixins import ExtendedModelSerializer

User = get_user_model()


########################
# CARTS
########################

class CartUserRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения корзины пользователя по id пользователя"""

    products = ProductShortSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'products',
            'created_at',
            'updated_at',
        )


class MeCartRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения своей корзины пользователем"""

    products = ProductShortSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'products',
        )


########################
# CART_PRODUCTS_ADD
########################

class ProductCartRepresentationSerializer(serializers.ModelSerializer):
    """Вложенный сериализатор для вывода"""
    id = serializers.IntegerField(source='product.id')
    name = serializers.CharField(source='product.name')

    class Meta:
        model = CartProduct
        fields = (
            'id',
            'name',
            'amount',
        )


class CartProductRepresentationSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода"""
    products = ProductCartRepresentationSerializer(many=True,
                                                   source='cart_products')

    class Meta:
        model = Cart
        fields = (
            'id',
            'products',
        )
        read_only_fields = fields


class ProductCartCreateUpdateSerializer(ExtendedModelSerializer):
    """Сериализатор для товаров.
    Используется при добавлении товара в корзину"""

    id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),
                                            source='cart_products')
    amount = serializers.IntegerField()

    class Meta:
        model = CartProduct
        fields = (
            'id',
            'amount',
        )


class CartProductCreateUpdateSerializer(ExtendedModelSerializer):
    """Сериализатор для добавления товаров в корзину"""

    products = ProductCartCreateUpdateSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'products',
        )

    def create_cart_products(self, cart, products_data):
        cart_products = []
        for product_data in products_data:
            product = product_data['cart_products']
            amount = product_data['amount']

            if CartProduct.objects.filter(cart=cart, product=product).exists():
                raise serializers.ValidationError(
                    f'{product.name} уже есть в корзине.')

            cart_products.append(
                CartProduct(cart=cart, product=product, amount=amount)
            )

        CartProduct.objects.bulk_create(cart_products)

    def update(self, cart, validated_data):
        products_data = validated_data.pop('products')
        super().update(cart, validated_data)
        self.create_cart_products(cart, products_data)
        cart.save()
        return cart

    def to_representation(self, instance):
        request = self.context.get('request')
        return CartProductRepresentationSerializer(instance,
                                                   context={
                                                       'request': request}).data


##########################
# CART_PRODUCTS_DELETE
##########################

class CartProductDeleteSerializer(serializers.Serializer):
    """Сериализатор для удаления товара из корзины"""
    product_id = serializers.IntegerField()

    def validate(self, data):
        user = self.context['request'].user
        product_id = data.get('product_id')
        if not CartProduct.objects.filter(cart__user=user,
                                          product_id=product_id).exists():
            raise serializers.ValidationError('Товар не найден в корзине')
        return data

    def save(self):
        user = self.context['request'].user
        product_id = self.validated_data['product_id']
        CartProduct.objects.filter(cart__user=user,
                                   product_id=product_id).delete()


##########################
# CART_PRODUCTS_AMOUNT
##########################
class IncreaseCartProductQuantitySerializer(serializers.Serializer):
    """Сериализатор для увеличения количества товара в корзине на 1"""
    product_id = serializers.IntegerField()

    def validate(self, data):
        user = self.context['request'].user
        product_id = data.get('product_id')
        try:
            cart_product = CartProduct.objects.get(cart__user=user,
                                                   product_id=product_id)
        except CartProduct.DoesNotExist:
            raise serializers.ValidationError('Товар не найден в корзине')
        return data

    def save(self):
        user = self.context['request'].user
        product_id = self.validated_data['product_id']
        cart_product = CartProduct.objects.get(cart__user=user,
                                               product_id=product_id)
        cart_product.amount += 1
        cart_product.save()
        return cart_product


class ReduceCartProductQuantitySerializer(serializers.Serializer):
    """Сериализатор для уменьшения количества товара в корзине на 1"""
    product_id = serializers.IntegerField()

    def validate(self, data):
        user = self.context['request'].user
        product_id = data.get('product_id')
        try:
            cart_product = CartProduct.objects.get(cart__user=user,
                                                   product_id=product_id)
        except CartProduct.DoesNotExist:
            raise serializers.ValidationError('Товар не найден в корзине')
        return data

    def save(self):
        user = self.context['request'].user
        product_id = self.validated_data['product_id']
        cart_product = CartProduct.objects.get(cart__user=user,
                                               product_id=product_id)
        if cart_product.amount > 1:
            cart_product.amount -= 1
            cart_product.save()
        else:
            cart_product.delete()
        return cart_product

