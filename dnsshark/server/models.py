from django.db import models
from django.contrib.auth.models import User


class DomainRule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255)
    action = models.CharField(
        max_length=10, choices=[("allow", "Allow"), ("block", "Block")]
    )

    def __str__(self):
        return f"{self.domain} - {self.action}"
