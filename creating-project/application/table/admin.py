from django.contrib import admin
from table.models import Field, CsvPath

class FieldAdmin(admin.ModelAdmin):
    pass

class CsvPathAdmin(admin.ModelAdmin):
    pass

admin.site.register(Field, FieldAdmin)
admin.site.register(CsvPath, CsvPathAdmin)
