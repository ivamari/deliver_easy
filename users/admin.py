from django.contrib import admin

from users.models.users import User


# Register your models here.
@admin.register(User)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'phone_number', 'first_name', 'last_name',
    )

