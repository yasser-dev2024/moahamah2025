from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ روابط المستخدمين (تسجيل - دخول - تسجيل خروج - لوحة تحكم)
    path('', include('users.urls')),

    # ✅ روابط القضايا
    path('lawsuits/', include('lawsuits.urls')),
]
