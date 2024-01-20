from django.contrib import admin
from django.contrib.auth.models import Group
from . models import Doctor, Schedule,Department,Appointment



admin.site.site_header='Doctor Appointment'
admin.site.site_title='Administration'
admin.site.index_title='Doctor Appointment'



# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['deptid','deptname','deptdesc']
    search_fields=['deptname']
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=['dname','dqua','aboutdoc','dspec','departments']
    raw_id_fields=['dept']

    search_fields=['dname','dqua']

    def departments(self,obj):
        return obj.dept.deptname

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display=['doctors', 'days','t_slot']
    raw_id_fields=['doctor']

    def doctors(self,obj):
        return obj.doctor.dname
    
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=('patients','doctors', 'appmadeon', 'appdate')

    def patients(self, obj):
        return obj.patient.first_name+" "+obj.patient.last_name
    
    def doctors(self, obj):
        return obj.doctor.dname
    
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    
