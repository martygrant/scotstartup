from django.contrib import admin
from scotstartup.models import UserProfile
from scotstartup.models import Company

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Company, CompanyAdmin)
admin.site.register(UserProfile)
