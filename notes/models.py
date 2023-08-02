from django.db import models


# Create your models here.
class NoteModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        return self.title
