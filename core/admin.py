from django.contrib import admin
from core.models import Station, Train, TrainStation

# Register your models here.

admin.site.register(Station)
admin.site.register(Train)
admin.site.register(TrainStation)