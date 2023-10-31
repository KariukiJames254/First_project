from django.db import models

from base.models import GenericBaseModel, BaseModel, State
from users.models import SpinSchoolUsers


class Student(SpinSchoolUsers):
    Fees = models.DecimalField(decimal_places=2, max_digits=20)

    class Meta:
        verbose_name = "Student"

    def __str__(self):
        return self.first_name


class Teacher(SpinSchoolUsers):
    class Meta:
        verbose_name = "Teacher"

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Classes(GenericBaseModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=State.default_state)

    @classmethod
    def default_class(cls):
        try:
            state = cls.objects.get(name="form1")
            return state
        except Exception:
            return None

    class Meta:
        verbose_name = "Class"

    def __str__(self):
        return self.name


class Subject(GenericBaseModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=State.default_state)

    class Meta:
        verbose_name = "Subject"

    def __str__(self):
        return self.name


class Grades(BaseModel):
    grade = models.CharField(max_length=4, null=False, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=State.default_state)

    class Meta:
        verbose_name = "Grade"

    def __str__(self):
        return self.grade


class JointStudentSubjectClass(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Classes = models.ForeignKey(Classes, on_delete=models.CASCADE, default=Classes.default_class)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=State.default_state)
