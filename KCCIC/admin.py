from django.contrib import admin

from KCCIC.models import *
# Register your models here.
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Advisor)

admin.site.register(Course)
admin.site.register(CourseIdentifier)
admin.site.register(Meeting)
admin.site.register(StudentSchedule)
admin.site.register(Instructor)
admin.site.register(Location)