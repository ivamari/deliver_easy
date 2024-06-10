from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cafes.views.cafes import CafeViewSet
from cafes.views.categories import CategoryView, CategoryCookingTimeView
from cafes.views.employees import EmployeeView
from cafes.views.departments import DepartmentView
from cafes.views.positions import PositionView
from cafes.views.products import ProductCafeView

router1 = DefaultRouter()
router2 = DefaultRouter()
router3 = DefaultRouter()

router1.register(r'', CafeViewSet, 'cafes')
router1.register(r'(?P<cafe_id>[^/.]+)/employees', EmployeeView,
                 basename='employees')
router1.register(r'(?P<cafe_id>[^/.]+)/departments', DepartmentView,
                 basename='departments')
router2.register(r'(?P<department_id>[^/.]+)/positions', PositionView,
                 basename='positions')
router3.register(r'categories', CategoryView, basename='categories')
router3.register(r'(?P<category_id>[^/.]+)/category-cooking-time',
                 CategoryCookingTimeView,
                 basename='category_cooking_time')
# router3.urls('', ProductView, 'products')
router1.register(r'(?P<cafe_id>[^/.]+)/products', ProductCafeView,
                 basename='products')


urlpatterns = [
    path('cafes/', include(router1.urls)),
    path('departments/', include(router2.urls)),
    path('products/', include(router3.urls)),
]
