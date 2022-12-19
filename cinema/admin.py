from django.contrib import admin
from .models import Screen , MovieShow,Cinema,City,Facility,MovieshowSeat


admin.site.register(Screen)
admin.site.register(MovieShow)
admin.site.register(Facility)
admin.site.register(Cinema)
admin.site.register(City)
admin.site.register(MovieshowSeat)

