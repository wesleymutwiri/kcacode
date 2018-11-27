from django.contrib import admin
from assurance.models import Report, Category, Feedback

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    def has_add_permission(self,request,obj=None):
        return False
    exclude = ['date', 'user']

class ReportAdmin(admin.ModelAdmin):
    exclude = ['date', 'user']
admin.site.register(Report)
admin.site.register(Category)
admin.site.register(Feedback)
