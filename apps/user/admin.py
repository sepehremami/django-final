from django.contrib import admin
from .models import *
# from .permissions import *

admin.site.register(User)
admin.site.register(Membership)
admin.site.register(UserRewardLog)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_display=['user','receiver','province','city','addr','zip_code','phone','is_default',]