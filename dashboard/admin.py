from django.contrib import admin

# Register your models here.

from .models import Groups
from .models import Hosts

admin.site.register(Groups)
admin.site.register(Hosts)
