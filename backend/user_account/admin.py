from django.contrib import admin
from .models import User, UserDeviceToken, UserProfile
# Register your models here.
admin.site.register(User)
admin.site.register(UserDeviceToken)
admin.site.register(UserProfile)
