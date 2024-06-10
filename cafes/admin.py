from django.contrib import admin
from cafes.models.cafes import Cafe
from cafes.models.carts import Cart, CartProduct
from cafes.models.categories import Category, CategoryCookingTime
from cafes.models.employees import Employee
from cafes.models.orders import OrderStatus, Order, OrderProduct
from cafes.models.positions import Position
from cafes.models.products import Product
from cafes.models.replacements import Replacement, ReplacementStatus
from cafes.models.departments import Department
from leaflet.admin import LeafletGeoAdmin


################
# CAFES
################
@admin.register(Cafe)
class CafeAdmin(LeafletGeoAdmin):
    list_display = ('id', 'name', 'owner',)


################
# EMPLOYEES
################

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'cafe', 'position')


################
# STRUCTURES
################

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'department',)


################
# REPLACEMENTS
################

@admin.register(Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_start', 'time_end',)
    list_display_links = ('id', 'time_start',)


@admin.register(ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    list_display_links = ('name',)


################
# PRODUCTS
################

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    list_display_links = ('code', 'name',)


@admin.register(CategoryCookingTime)
class CategoryCookingTimeAdmin(admin.ModelAdmin):
    list_display = ('category', 'cooking_time',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    filter_horizontal = ('cafe',)


################
# CARTS
################

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'amount',)


################
# ORDERS
################

@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'order_date', 'order_time',)


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'amount',)
