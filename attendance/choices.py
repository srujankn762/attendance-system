from django.db import models


class Role(models.TextChoices):
    SUPER_ADMIN = 'SUPER_ADMIN', 'Super Admin'
    ADMIN = 'ADMIN', 'Admin'
    HR = 'HR', 'HR'
    EMPLOYEE = 'EMPLOYEE', 'Employee'


class Department(models.TextChoices):
    BACKEND = 'Backend', 'Backend'
    FRONTEND = 'Frontend', 'Frontend'
    DEVOPS = 'Devops', 'Devops'
    HR = 'HR', 'HR'
    SALES = 'Sales', 'Sales'


class AttendanceStatus(models.TextChoices):
    PRESENT = 'PRESENT', 'Present'
    ABSENT = 'ABSENT', 'Absent'
    LEAVE = 'LEAVE', 'Leave'
