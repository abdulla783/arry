from django.contrib import admin
from resume.models import Home, Contact

# Register your models here.

admin.site.register(Home)
admin.site.register(Contact)

admin.site.site_title = 'ARRY'
admin.site.site_header = 'ARRY'
