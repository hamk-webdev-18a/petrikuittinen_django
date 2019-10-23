from django.db import models

# Create your models here.
class Dictionary(models.Model):
    word = models.CharField(max_length=200)
    definition = models.CharField(max_length=200)
    def __str__(self):
        return self.word+" = "+self.definition

    class Meta:
        indexes = [
            models.Index(fields=['word', 'definition']),
        ]
                                    
