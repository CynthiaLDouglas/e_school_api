from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# define fields
# https://docs.djangoproject.com/en/3.0/ref/models/fields/
class Course(models.Model):
    name = models.CharField(max_length=100)
    MATH = 'Math'
    SCIENCE = 'Science'
    HUMANITIES = 'Humanities'
    ENGLISH = 'English'
    SUBJECT_CHOICES = [
          (MATH, 'Math'),
          (SCIENCE, 'Science'),
          (HUMANITIES, 'Humanities'),
          (ENGLISH, 'English'),
      ]
    subject = models.CharField(
          max_length=12,
          choices=SUBJECT_CHOICES,
          default=HUMANITIES,
      )
    course_description = models.CharField(max_length=2000, default='')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
  )

    def __str__(self):
      # This must return a string
        return self.name

    def as_dict(self):
        """Returns dictionary version of Mango models"""
        return {
            'id': self.id,
            'name': self.name,
            'subject': self.subject,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'owner': self.owner
        }
