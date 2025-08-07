from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  # ✅ صفحة المستخدم بعد الدخول
    path('', views.login_view),  # ✅ أي دخول للموقع يوجه لصفحة الدخول
]
