from django.db import models

class DashboardItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
