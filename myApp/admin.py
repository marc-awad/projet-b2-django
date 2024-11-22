#Importing all necessary dependencies
from django.contrib import admin
from .models import Conges
 
# Save the template in the administration interface
admin.site.register(Conges)