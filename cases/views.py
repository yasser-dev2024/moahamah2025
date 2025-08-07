from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CaseForm
from .models import Case

@login_required
def case_list(request):
    cases = Case.objects.filter(user=request.user)
    return render(request, 'cases/case_list.html', {'cases': cases})

@login_required
def case_create(request):
    if request.method == 'POST':
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            case = form.save(commit=False)
            case.user = request.user
            case.save()
            return redirect('case_list')
    else:
        form = CaseForm()
    return render(request, 'cases/case_create.html', {'form': form})
