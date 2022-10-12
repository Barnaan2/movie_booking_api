from django.contrib import admin
from system_admin.models import Cast, Cinema, City, Crew,Movie


admin.site.register(City)
admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Crew)
admin.site.register(Cast)

# Register your models here.
