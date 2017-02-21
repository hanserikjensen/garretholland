from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def create_course(self, name):
        course = Course(course_name=name)
        course.save()
        return course


    def add_description(self, description):
        print ">>>got description-->>>", description
        description = Description.objects.create(description=description)

        return description


    def destroy_course(self, course):
        course_destroy = Course.objects.filter(id=course).delete()


    def create_comment(self, comment, course):
        comment = Comments.objects.create(comment=comment, course=course)

        return comment


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()
    #comments
    #description

    def __str__(self):
        return self.course_name

class Description(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True,)

    objects = CourseManager()

    def __str__(self):
        return self.description

class Comments(models.Model):
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    course = models.ForeignKey(Course, related_name="comments")
    objects = CourseManager()

    def __str__(self):
        return self.comment
