from django.contrib import admin
from .models import *
# from .permissions import *

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Membership)
admin.site.register(UserRewardLog)
