from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Firstname','Lastname','Email','Contact',)
admin.site.register(Student,StudentAdmin)



class UserAdmin(admin.ModelAdmin):
    list_display = ['Firstname','Lastname','Contact','Email',]
admin.site.register(User,UserAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['Firstname','Lastname','Contact',]

admin.site.register(Teacher,TeacherAdmin)


