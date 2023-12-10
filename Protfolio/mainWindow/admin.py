from django.contrib import admin
from .models import New
from .models import Info
from .models import Biography

admin.site.register(New)
admin.site.register(Info)
admin.site.register(Biography)