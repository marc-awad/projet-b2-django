from django.shortcuts import render
from .forms import AskConges 

def demande_conges(request):
    if request.method == 'POST':
        form = AskConges(request.POST)
        if form.is_valid():
            form.save()
            print("Congés pris en compte")
    else:
        form = AskConges()
    return render(request, 'demande_conges.html', context={'form': form})
