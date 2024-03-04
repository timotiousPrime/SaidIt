from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


# Create your models here.
class Job_Title(models.Model):
    title = models.CharField(max_length=48)

    def __str__(self) -> str:
        return self.title


class Interest(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self) -> str:
        return self.name


class Employment_History(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="emploment_history"
    )
    company = models.CharField(max_length=48)
    position = models.ForeignKey(
        Job_Title, on_delete=models.CASCADE, blank=True, null=True
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.position} @ {self.company}"


class User_Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    first_name = models.CharField(max_length=48, blank=True, null=True)
    surname = models.CharField(max_length=48, blank=True, null=True)
    email = models.CharField(max_length=48, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, default="")
    date_of_birth = models.DateTimeField(
        blank=True, null=True, default=timezone.make_aware(datetime(2000, 1, 1))
    )
    title = models.CharField(max_length=5, blank=True, null=True, default="")
    interests = models.ManyToManyField("Interest", blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.surname}"
