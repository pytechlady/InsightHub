from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class User(AbstractUser):
    organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    role = models.CharField(
        max_length=20,
        choices=[('admin', 'Admin'), ('analyst', 'Analyst'), ('viewer', 'Viewer')],
        default='viewer',
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
