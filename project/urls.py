from django.contrib import admin
from django.urls import path
from myApp.views import demande_conges

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conges/',demande_conges),
]
