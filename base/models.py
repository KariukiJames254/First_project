from django.db import models
import uuid


# Create your models her
class BaseModel(models.Model):
    id = models.UUIDField(max_length=100, primary_key=True, default=uuid.uuid4)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "BaseModel"

    def __str__(self):
        return self.id


class GenericBaseModel(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "GenericBaseModel"

    def __str__(self):
        return self.name


class State(models.Model):
    id = models.UUIDField(max_length=100, primary_key=True,  default=uuid.uuid4)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def default_state(cls):
        try:
            state = cls.objects.get(name="Active")
            return state
        except Exception:
            return None

    @classmethod
    def disabled_state(cls):
        try:
            state = cls.objects.get(name="Disabled")
            return state
        except Exception:
            return None
