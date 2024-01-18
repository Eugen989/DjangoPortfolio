from django.contrib import admin
from .models import New
from .models import Info
from .models import Biography
from .models import Portfolio
from .models import Activity



admin.site.register(New)
admin.site.register(Info)
admin.site.register(Activity)
admin.site.register(Biography)
admin.site.register(Portfolio)
