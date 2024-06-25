from django.urls import path

from users.views.clients import (
    RegistrationClientView,
    MeClientView,
    ClientView
)
from users.views.employees import (
    RegistrationEmployeeView,
    MeEmployeeView,
    EmployeeUpdatedView
)


urlpatterns = [
    path('users/client/reg/', RegistrationClientView.as_view(),
         name='reg'),
    path('users/employee/reg/', RegistrationEmployeeView.as_view(),
         name='reg'),
    path('users/client/me/', MeClientView.as_view(), name='me'),
    path('users/employee/me/', MeEmployeeView.as_view(), name='me'),
    path('users/employee/<int:user_id>/', EmployeeUpdatedView.as_view(),
         name='user-employee'),
    path('users/client/<int:user_id>/', ClientView.as_view(),
         name='user-client'),
]
