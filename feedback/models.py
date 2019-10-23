from django.db import models

# Create your models here.

class Feedback(models.Model):
    #grade = models.PositiveIntegerField()
    good = models.TextField()
    bad = models.TextField()
    ideas = models.TextField()
    date = models.DateTimeField('date sent', auto_now_add=True)
    def __str__(self):
        return str(self.date)
                                
