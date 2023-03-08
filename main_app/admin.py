from django.contrib import admin
from .models import Chore, Kid, Parent


# Register your models here.

admin.site.register(Chore)
admin.site.register(Kid)
admin.site.register(Parent)