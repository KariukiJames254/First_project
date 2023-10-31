from django.contrib.auth.models import User
from django.db import models

from base.models import State


# Create your models here.
class SpinSchoolUsers(User):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
    my_gender_choices = [
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
        (OTHER, "OTHER"),
    ]
    gender = models.CharField(max_length=10, choices=my_gender_choices, default=OTHER)
    mobile = models.IntegerField(null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=State.default_state)

    class Meta:
        verbose_name = "SpinSchoolUser"

    def __str__(self):
        return self.username
