from django.contrib import admin
from hospitalapp.models import Departments, Doctors, Index, IndexDoctor, News, Patient, Popular, Appointment


# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Index)
admin.site.register(IndexDoctor)
admin.site.register(News)
admin.site.register(Patient)
admin.site.register(Popular)
admin.site.register(Appointment)
