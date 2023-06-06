from django.contrib import admin
from cars.models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('TIME INFORMATIO',{'fields':['year']}),
        ('CAR INFORMATION',{'fields':['brand']})
    ]


admin.site.register(Car,CarAdmin)