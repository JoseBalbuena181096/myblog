from django.contrib import admin
from .models import Home
from .models import Suscribers
from .models import Contact

# Register your models here.
admin.site.register(Home)
admin.site.register(Suscribers)
admin.site.register(Contact)

