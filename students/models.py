from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Student(models.Model):
    name = models.CharField(_("Name"), max_length=50,null=True,blank=True)
    email = models.EmailField(_("Email"), max_length=254,null=True,blank=True)
    phone = models.CharField(_("Phone"),max_length=15,null=True,blank=True)
    studentId = models.IntegerField(_("Student Id"),null=True,blank=True)
    reason = models.TextField(_("Reason"), null=True,blank=True)
    rightAns = models.IntegerField(_("Right quiz ans"),null=True,blank=True)
    totalQuiz = models.IntegerField(_("Total quizzes"),null=True,blank=True)

    def __str__(self):
        return self.name
    