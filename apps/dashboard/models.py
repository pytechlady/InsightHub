from django.db import models
from analysis.models import AnalysisTask

# Create your models here.
class Insight(models.Model):
    analysis = models.ForeignKey(AnalysisTask, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
