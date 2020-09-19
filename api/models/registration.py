from django.db import models
from .course import Course
from .user import User

class Registration(models.Model):
    semester = models.CharField(max_length=10)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_enrolled = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{student_enrolled} enrolled into {course_name}"

    def as_dict(self):
        """Returns dictionary version of Mango models"""
        return {
            'id': self.id,
            'course_name': self.course_name,
            'student_enrolled': self.student_enrolled
        }
