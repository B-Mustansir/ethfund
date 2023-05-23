from django.contrib import admin

from Ethfund_app.models import Category, Projects


admin.site.site_header = "EthFund | Admin"

admin.site.register(Category)
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display =  ['id','projectname','added_on','is_approved']
admin.site.register(Projects,ProjectAdmin)



