from django.contrib import admin
from first_app.models import StudentModel, StudentInfoModel, TeacherInfoModel, EmployeeModel, ManagerModel, FriendModel, MeModel
# Register your models here.

admin.site.register(StudentModel)
# admin.site.register(StudentInfoModel)
# admin.site.register(TeacherInfoModel)
# admin.site.register(EmployeeModel)
# admin.site.register(ManagerModel)

@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'designation']


@admin.register(ManagerModel)
class ManagerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'designation', 'take_interview', 'hiring']


@admin.register(FriendModel)
class FriendModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'section', 'attendence', 'home_work']



@admin.register(MeModel)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'section', 'attendence', 'home_work']


