from django.contrib import admin
from .models import *


admin.site.site_header='Green City'
admin.site.site_title='Admin'
admin.site.index_title='Green City'



# Register your models here.
admin.site.register(MyUser)
admin.site.register(StudentForm)