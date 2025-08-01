from django.db import models

class User(models.Model):
    role = models.CharField(max_length=100)
    content = models.CharField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role + ": " + self.content