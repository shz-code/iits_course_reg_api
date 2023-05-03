from django.contrib import admin
from .models import Student
from import_export import resources

class StudentsResources(resources.ModelResource):
    class Meta:
        model = Student
        fields = ('name','email','phone','studentId','reason','rightAns','totalQuiz','submission_date')
        export_order = ('studentId','name','email','phone','reason','rightAns','totalQuiz','submission_date')

# Register your models here.
admin.site.register(Student)