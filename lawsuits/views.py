from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lawsuit
from .forms import LawsuitForm

# ✅ إنشاء قضية جديدة
@login_required
def lawsuit_create(request):
    if request.method == 'POST':
        form = LawsuitForm(request.POST)
        if form.is_valid():
            lawsuit = form.save(commit=False)
            lawsuit.created_by = request.user
            lawsuit.save()
            return redirect('list')  # إلى صفحة قائمة القضايا
    else:
        form = LawsuitForm()
    return render(request, 'lawsuits/create.html', {'form': form})

# ✅ عرض القضايا الخاصة بالمستخدم الحالي
@login_required
def lawsuit_list(request):
    lawsuits = Lawsuit.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, 'lawsuits/list.html', {'lawsuits': lawsuits})
