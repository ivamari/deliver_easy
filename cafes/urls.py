from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cafes.views.cafes import CafeView, CafeSearchView, CafeDepartmentView
from cafes.views.carts import CartView, MeCartView
from cafes.views.categories import CategoryView, CategoryCookingTimeView
from cafes.views.departments import DepartmentView
from cafes.views.employees import EmployeeView
from cafes.views.positions import PositionView
from cafes.views.products import ProductCafeView, ProductView

router1 = DefaultRouter()
router2 = DefaultRouter()
router3 = DefaultRouter()
router4 = DefaultRouter()

router1.register(r'search', CafeSearchView, 'organisations-search')
router1.register(r'', CafeView, 'cafes')
router4.register(r'', CafeDepartmentView,
                 'cafe_departments')
router1.register(r'(?P<cafe_id>[^/.]+)/employees', EmployeeView,
                 basename='employees')
router2.register(r'(?P<department_id>[^/.]+)/positions', PositionView,
                 basename='positions')
router3.register(r'categories', CategoryView, basename='categories')
router3.register(r'(?P<category_id>[^/.]+)/category-cooking-time',
                 CategoryCookingTimeView,
                 basename='category_cooking_time')
router3.register('', ProductView, 'products')
router1.register(r'(?P<cafe_id>[^/.]+)/products', ProductCafeView,
                 basename='products')
router2.register(r'', DepartmentView, basename='departments')

urlpatterns = [
    path('cafes/', include(router1.urls)),
    path('departments/', include(router2.urls)),
    path('products/', include(router3.urls)),
    path('clients/<int:client_id>/cart/', CartView.as_view(), name='client-cart'),
    path('clients/cart/me/', MeCartView.as_view(), name='me-client-cart'),
    path('cafe-departments/', include(router4.urls)),
]
