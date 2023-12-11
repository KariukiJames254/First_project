from django.db import models

from base.models import GenericBaseModel, BaseModel, State
from users.models import SpinSchoolUsers


class Student(BaseModel):
    user = models.ForeignKey(SpinSchoolUsers, on_delete=models.CASCADE)
    Fees = models.DecimalField(decimal_places=2, max_digits=20)
    Arrears = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    registration_number = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        verbose_name = "Student"

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


class Teacher(BaseModel):
    user = models.ForeignKey(SpinSchoolUsers, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Teacher"

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


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

    @classmethod
    def default_subject(cls):
        try:
            subject = cls.objects.get(name="Mathematics")
            return subject
        except Exception:
            return None

    @classmethod
    def disabled_subject(cls):
        try:
            subject = cls.objects.get(name="Geography")
            return subject
        except Exception:
            return None


class Grades(BaseModel):
    grade = models.CharField(max_length=4, null=False, blank=False)
    name = models.CharField(max_length=20, default="Average")
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=State.default_state)

    class Meta:
        verbose_name = "Grade"

    def __str__(self):
        return '%s - %s' % (self.grade, self.name)

    @classmethod
    def default_grade(cls):
        try:
            state = cls.objects.get(name="C")
            return state
        except Exception:
            return None


class JointStudentSubjectClass(models.Model):
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Classes = models.ForeignKey(Classes, on_delete=models.CASCADE, default=Classes.default_class)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=State.default_state)


class StudentScore(BaseModel):
    student_grade = models.ForeignKey(Grades, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField(default=50)
    form = models.ForeignKey(Classes, on_delete=models.CASCADE)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=Subject.default_subject)

    def __str__(self):
        return '%s' % self.score
