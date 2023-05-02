from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Option(models.Model):
    title = models.CharField(_("Title"),max_length=255)
    isCorrect = models.BooleanField(_("IsCorrect"),default=False)

    def __str__(self):
        return self.title
    
class DeadLine(models.Model):
    deadline = models.DateTimeField(_("Deadline"),null=True,blank=True)

    def __str__(self):
        return f"{self.deadline}"
    
    class Meta:
        verbose_name_plural = "Deadline"

class Quiz(models.Model):
    question = models.CharField(_("Name"),max_length= 255)
    options = models.ManyToManyField(Option,_("Options"))
    
    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.question