from django.shortcuts import render, redirect, get_object_or_404
from .forms import AskConges , AdminstratorConnection
from .models import Conges
from .sending_mail import validation, cancel
from time import sleep
from django.contrib import messages


def demande_conges(request):
    if request.method == 'POST':
        form = AskConges(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get("date")
            end_date = form.cleaned_data.get("end_date")
            if start_date > end_date:
                form.add_error('end_date', "La date de fin doit être après la date de début.")
            else:
                messages.success(request, 'Votre demande a été envoyée avec succès.')
                form.save()
                sleep(0.5)
                return redirect('redirection/')

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
            conge.status = "validee"
            validation(conge)
        elif action == 'refuser':
            conge.status = "refusee"
            cancel(conge)
        else:
            conge.status = "en_attente"

        conge.save()
    return render(request, 'admin.html', context={'conges': conges})

def redirection_page(request):
    return render(request, 'redirection.html')

