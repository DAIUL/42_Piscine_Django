from django.contrib import admin
from .models import Tip, UserInfos
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "created_at")
    
class UserInfosAdmin(BaseUserAdmin):
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    search_fields = ('username',)
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(UserInfos, UserInfosAdmin)