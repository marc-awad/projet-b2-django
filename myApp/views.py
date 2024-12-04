#Importing all necessary dependencies
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AskConges , AdminstratorConnection
from .models import Conges
from .sending_mail import validation, cancel
from time import sleep
from django.contrib import messages
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

# View for leave request form 
def demande_conges(request):
    if request.method == 'POST':
        form = AskConges(request.POST)
        if form.is_valid():
            #Check if the date is valid
            start_date = form.cleaned_data.get("date")
            end_date = form.cleaned_data.get("end_date")
            today = datetime.today().date()
            if start_date > end_date:
                form.add_error('end_date', "La date de fin doit être après la date de début.")
            elif start_date < today:
                form.add_error('date', "La date de début ne peut pas être dans le passé.") 
            else:
                #If the date is valid we save the form and send the email
                messages.success(request, 'Votre demande a été envoyée avec succès.')
                form.save()
                sleep(0.5)
                return redirect('redirection/')

    else:
        form = AskConges()
    return render(request, 'demande_conges.html', context={'form': form})

#View for the home page 
def home_page(request):
    if request.method == 'POST':
        form = AdminstratorConnection(request.POST)
        if form.is_valid():
            PASSWORD = os.getenv("PASSWORD")
            USERNAME = os.getenv("USERNAME")
            if(form.cleaned_data['username'] == USERNAME and form.cleaned_data['password'] == PASSWORD):
                return redirect('administrateur/')
            else:
                messages.error(request, "Identifiants incorrects.")
    else:
        form = AdminstratorConnection()
            
    return render(request, 'index.html', context={'form': form})

#View for the admin page
def admin_page(request):
    conges = Conges.objects.all()
    if request.method == 'POST':
        conge_id = request.POST['id']
        action = request.POST['action']

        conge = get_object_or_404(Conges, id=conge_id)

        #Checking the button actions
        if action == 'valider':
            conge.status = "validee"
            validation(conge)
        elif action == 'refuser':
            conge.status = "refusee"
            cancel(conge)
        else:
            conge.status = "en_attente"

        #Saving the status
        conge.save()
    return render(request, 'admin.html', context={'conges': conges})

# View for the redirection page
def redirection_page(request):
    return render(request, 'redirection.html')

