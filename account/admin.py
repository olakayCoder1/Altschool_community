from django.contrib import admin
from .models import User  , Profile
from django.contrib.auth.admin import UserAdmin



class CustomUserAdminConfig(UserAdmin):     
    model = User
    search_fields = ('username', 'email',)   
    list_filter = ('username', 'email', 'is_active', 'is_staff')
    ordering = ('-created_at',)
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser') 
    fieldsets = (
        (None, {'fields': ('username', 'email',)}), 
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username' , 'email',     'password1', 'password2', 'is_active', 'is_staff' )} 
         ),
    )





admin.site.register(User, CustomUserAdminConfig) 
admin.site.register(Profile) 
        