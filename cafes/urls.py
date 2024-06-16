from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cafes.views.cafes import CafeView, CafeSearchView, CafeDepartmentView
from cafes.views.carts import (CartView, MeCartView, MeCartDeleteView,
                               IncreaseProductQuantityView,
                               ReduceProductQuantityView)
from cafes.views.categories import CategoryView
from cafes.views.departments import DepartmentView
from cafes.views.employees import EmployeeView
from cafes.views.positions import PositionView
from cafes.views.products import ProductCafeView, ProductView

router_cafe = DefaultRouter()
router_departments = DefaultRouter()
router_categories = DefaultRouter()
router_cafe_departments = DefaultRouter()

router_cafe.register(r'search', CafeSearchView, 'organisations-search')
router_cafe.register(r'', CafeView, 'cafes')
router_cafe_departments.register(r'', CafeDepartmentView,
                                 'cafe_departments')
router_cafe.register(r'(?P<cafe_id>[^/.]+)/employees', EmployeeView,
                     basename='employees')
router_departments.register(r'(?P<department_id>[^/.]+)/positions',
                            PositionView,
                            basename='positions')
router_categories.register(r'categories', CategoryView, basename='categories')
router_categories.register('', ProductView, 'products')
router_cafe.register(r'(?P<cafe_id>[^/.]+)/products', ProductCafeView,
                     basename='products')
router_departments.register(r'', DepartmentView, basename='departments')

urlpatterns = [
    path('cafes/', include(router_cafe.urls)),
    path('departments/', include(router_departments.urls)),
    path('products/', include(router_categories.urls)),
    path('clients/<int:client_id>/cart/', CartView.as_view(),
         name='client-cart'),
    path('clients/cart/me/', MeCartView.as_view(), name='me-client-cart'),
    path('cafe-departments/', include(router_cafe_departments.urls)),
    path('clients/cart/me/<int:product_id>/delete/', MeCartDeleteView.as_view(),
         name='me-client-cart'),
    path('clients/cart/me/<int:product_id>/increase-quantity/',
         IncreaseProductQuantityView.as_view(),
         name='increase-product-quantity'),
    path('clients/cart/me/<int:product_id>/reduce-quantity/',
         ReduceProductQuantityView.as_view(), name='reduce-product-quantity'),
]
