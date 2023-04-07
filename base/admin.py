from django.contrib import admin
from . models import Users, Tasks, Categories, Reminders
# Register your models here.
admin.site.register(Users)
admin.site.register(Tasks)
admin.site.register(Categories)
admin.site.register(Reminders)
