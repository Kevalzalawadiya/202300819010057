from django.contrib import admin
from .models import Inquiry, CourseRegistration
from .services import EmailServices
# Register your models here.


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        EmailServices.send_inquiry_mail(obj)
        super(InquiryAdmin, self).save_model(request, obj, form, change)

@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','phone', 'course', 'is_confirmed')
    list_filter = ["course", "is_confirmed"]
