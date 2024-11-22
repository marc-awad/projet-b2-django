from django.shortcuts import render, redirect
from .forms import AskConges , AdminstratorConnection
from .models import Conges

def demande_conges(request):
    if request.method == 'POST':
        form = AskConges(request.POST)
        if form.is_valid():
            form.save()
            print("Congés pris en compte")
    else:
        form = AskConges()
    return render(request, 'demande_conges.html', context={'form': form})

def home_page(request):
    if request.method == 'POST':
        form = AdminstratorConnection(request.POST)
        if form.is_valid():
            if(form.cleaned_data['username'] == 'lorenzo' and form.cleaned_data['password'] == 'graven123'):
                return redirect('administrateur/')
    else:
        form = AdminstratorConnection()
            
    return render(request, 'index.html', context={'form': form})

def admin_page(request):
    conges = Conges.objects.all()
    if request.method == 'POST':
        conge_id = request.POST['id']
        action = request.POST['action']

        conge = Conges.objects.get(id=conge_id)
        if action == 'valider':
            conge.validate = True
        elif action == 'refuser':
            conge.validate = False
        conge.save()
    return render(request, 'admin.html', context={'conges': conges})

