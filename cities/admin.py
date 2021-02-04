from django.contrib import admin

# Register your models here.
from .models import Intity,Classification,Region

# class CityAdmin(admin.ModelAdmin):
#     list_display = ("name", "state",)

class IntityAdmin(admin.ModelAdmin):
    list_display = ("region", "classification","name")

# admin.site.register(City, CityAdmin)
admin.site.register(Region)
admin.site.register(Classification)
admin.site.register(Intity,IntityAdmin)


