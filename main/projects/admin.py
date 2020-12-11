from django.contrib import admin
from .models import Categories,MiniProjects, ProjectType
from adminsortable2.admin import SortableAdminMixin


@admin.register(MiniProjects)
class MyModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(Categories)
admin.site.register(ProjectType)