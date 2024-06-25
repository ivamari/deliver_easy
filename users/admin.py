from django.contrib import admin

from users.models.profile import Profile
from users.models.users import User
from django.utils.translation import gettext_lazy as _


class ProfileAdmin(admin.StackedInline):
    model = Profile
    fields = ('telegram_id',)


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    change_user_password_template = None

    fieldsets = (
        (None, {'fields': (
            'phone_number', 'email',)}),
        (_('Личная информация'),
         {'fields': ('first_name', 'last_name', 'username', 'birth_day', 'password',
                     'is_work_account')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',
                       # 'user_permissions'
                       ),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2',),
        }),
    )
    list_display = ('id', 'phone_number', 'email',)
    list_display_links = ('id', 'phone_number', 'email',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('id', 'email', 'phone_number',)
    ordering = ('-id',)
    # filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ('last_login',)

    inlines = (ProfileAdmin,)
