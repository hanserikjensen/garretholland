from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def create_course(self, name):
        print "!!!! Hit CourseManager create_course !!!!"
        course = Course(course_name=name)
        course.save()
        return course

    def add_description(self, description):
        print "!!!! hit CourseManager add_description !!!!"
        description = Description.objects.create(description=description)
        print "!!!!description is -------------->>>>>", description
        # description = Description(description=description)
        # description.save()
        return description

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = CourseManager()

    def __str__(self):
        return self.course_name

class Description(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True,)

    objects = CourseManager()

class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    objects = CourseManager()

# class Restaurant(models.Model):
#     place = models.OneToOneField(
#         Place,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     serves_hot_dogs = models.BooleanField(default=False)
#     serves_pizza = models.BooleanField(default=False)
#
#     def __str__(self):              # __unicode__ on Python 2
#         return "%s the restaurant" % self.place.name