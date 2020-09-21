from django.db import models
from django.contrib.auth import get_user_model

class Registration(models.Model):
    semester = models.CharField(max_length=10)
    course_name = models.ForeignKey('Course', on_delete=models.CASCADE)
    student_enrolled = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="classes")
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="registrations")

    def __str__(self):
        return f"{self.student_enrolled} enrolled into {self.course_name} by {self.owner}"
