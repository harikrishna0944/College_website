from django.contrib import admin

# Register your models here.
from . models import register_table,addadtimisionenquire_table,add_visiter_table,add_studentadmission_table
admin.site.register(register_table)
admin.site.register(addadtimisionenquire_table)
admin.site.register(add_visiter_table)
admin.site.register(add_studentadmission_table)