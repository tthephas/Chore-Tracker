from django.contrib import admin
from .models import Chore, Kid, Parent, Photo


# Register your models here.

admin.site.register(Chore)
admin.site.register(Kid)
admin.site.register(Parent)
admin.site.register(Photo)