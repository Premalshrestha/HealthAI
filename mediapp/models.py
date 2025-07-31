from django.db import models
from django.contrib.auth.models import User

class Family(models.Model):
    FamilyID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)

    family = models.ForeignKey(Family, null=True, blank=True, on_delete=models.SET_NULL, related_name='members')

    def __str__(self):
        return self.user.username if self.user else "No user"
