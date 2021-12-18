from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.

# Django admin provides a convenient way to associate related objects 
# on a single model managing page.
# Let's try to manage Lesson model together with Course model on 
# Course admin page.
# add a LessonInline class before CourseAdmin
# and update CourseAdmin class by adding a inlines list

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    # Update CourseAmin class after added LessonInline class
    # by adding a inlines list
    inlines = [LessonInline]


#Coding Practice: Customize Fields for Instructor Model
class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)

