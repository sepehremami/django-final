from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# from .permissions import *

admin.site.register(Membership)
admin.site.register(UserRewardLog)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display=['user','receiver','province','city','addr','zip_code','phone','is_default',]

class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    actions = ['make_staff',]

    def make_staff(self, request, queryset):
        queryset.update(is_staff=True)

    
    

admin.site.register(User, UserAdmin)