from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'first_name', 'surname')
    list_filter = ('email', 'first_name', 'surname', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'first_name', 'surname', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'surname')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'surname', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(NewUser, UserAdminConfig)
