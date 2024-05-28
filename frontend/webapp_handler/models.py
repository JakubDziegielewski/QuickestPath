from django.db import models

class TextEntry(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:200]  # Display the first 50 characters
