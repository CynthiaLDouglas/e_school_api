from django.db import models
from django.contrib.auth import get_user_model

class Registration(models.Model):
    semester = models.CharField(max_length=10)
    course_name = models.ForeignKey('Course', on_delete=models.CASCADE)
    student_enrolled = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_enrolled} enrolled into {self.course_name}"

    def as_dict(self):
        """Returns dictionary version of Mango models"""
        return {
            'id': self.id,
            'course_name': self.course_name,
            'student_enrolled': self.student_enrolled
        }
