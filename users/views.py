from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

# ✅ تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # تأكد أن لديك صفحة باسم dashboard
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
    return render(request, 'users/login.html')

# ✅ إنشاء حساب
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'اسم المستخدم مستخدم مسبقًا.')
            return redirect('register')

        user = User.objects.create(
            username=username,
            password=make_password(password),
            user_type=user_type
        )
        messages.success(request, 'تم إنشاء الحساب بنجاح. يمكنك تسجيل الدخول الآن.')
        return redirect('login')

    return render(request, 'users/register.html')

# ✅ تسجيل الخروج
def logout_view(request):
    logout(request)
    return redirect('login')

# ✅ الصفحة الرئيسية للمستخدم بعد الدخول
def dashboard(request):
    return render(request, 'users/dashboard.html')
