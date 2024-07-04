from django.db import models

class VisitorCounter(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Visitors: {self.count}"
