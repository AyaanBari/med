from django.contrib import admin
from django.contrib.auth.models import Group
from . models import Doctor, Schedule

admin.site.site_header='Doctor Appointment'
admin.site.site_title='Administration'
admin.site.index_title='Doctor Appointment'



# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=['dname','dqua','aboutdoc']
    search_fields=['dname','dqua']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display=['doctors', 'days','t_slot']
    raw_id_fields=['doctor']

    def doctors(self,obj):
        return obj.doctor.dname
