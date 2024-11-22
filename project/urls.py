from django.contrib import admin
from django.urls import path
from myApp.views import demande_conges, home_page, admin_page

urlpatterns = [
    path('',home_page, name='home_page'),
    path('conges/',demande_conges, name='demande_conges'),
    path('administrateur/',admin_page),
    path('admin/', admin.site.urls),
]
