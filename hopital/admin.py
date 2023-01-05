from django.contrib import admin
from hopital.models import Patient
from hopital.models import Service
from django.urls import reverse
from django.utils.safestring import mark_safe
class PatientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'numtel', 'dateNais')
    list_filter = ('nom', 'prenom', 'numtel', 'dateNais')
    date_hierarchy = 'dateNais'
    ordering = ('dateNais',)
    search_fields = ('nom', 'service')
    def service_link(self, pat):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:hopital_service_change", 
            args=(pat.service.pk,)),pat.service.nomSer
        ))
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nomSer', 'description')
    list_filter = ('nomSer','id')
    search_fields = ('nom', 'service')
    def apercu (self, service):
        text = service.description[:40]
        if len(service.description) > 40:
            return '{}...'.format(text)
        else:
            return text
admin.site.register(Patient, PatientAdmin)
admin.site.register(Service, ServiceAdmin)


