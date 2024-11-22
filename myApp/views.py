from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import AskConges , AdminstratorConnection
from .models import Conges
from .sending_mail import validation, cancel
from time import sleep


def demande_conges(request):
    if request.method == 'POST':
        form = AskConges(request.POST)
        if form.is_valid():
            form.save()
            print("Congés pris en compte")
            sleep(1)
            return redirect('/')

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


        conge = get_object_or_404(Conges, id=conge_id)
        print(conge)
        if action == 'valider':
            conge.validate = True
            validation(conge)
        elif action == 'refuser':
            conge.validate = False
            cancel(conge)
        conge.save()
    return render(request, 'admin.html', context={'conges': conges})

