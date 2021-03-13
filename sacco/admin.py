from django.contrib import admin
from .models import SaccoManager,SaccoMatatu,MatatuConductor,MatatuDriver,MatatuCollect

admin.site.register(SaccoManager)
admin.site.register(SaccoMatatu)
admin.site.register(MatatuConductor)
admin.site.register(MatatuDriver)
admin.site.register(MatatuCollect)