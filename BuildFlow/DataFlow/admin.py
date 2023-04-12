from django.contrib import admin

from .models import Project, Data, Address


class ProjectAdmin(admin.ModelAdmin):
    pass

class DataAdmin(admin.ModelAdmin):
    pass

class AddressAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Address, AddressAdmin)
