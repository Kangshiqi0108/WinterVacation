from django.contrib import admin
from .models import student,relatedresources,researchresults
# Register your models here.

admin.site.register(student)
admin.site.register(relatedresources)
admin.site.register(researchresults)

