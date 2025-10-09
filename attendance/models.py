import random
import string
from django.db import models, transaction, IntegrityError
from django.contrib.auth.models import AbstractUser
from .choices import Role, Department, AttendanceStatus


def generate_employee_id(department=None):
    """Generate a unique employee ID using department prefix + 5 random chars."""
    prefix_map = {
        "Backend": "BE",
        "Frontend": "FE",
        "Devops": "DV",
        "HR": "HR",
        "Sales": "SA",
    }
    prefix = prefix_map.get(department, "EMP")
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"{prefix}{random_part}"


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.EMPLOYEE
    )

    def __str__(self):
        return f"{self.username} ({self.role})"


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    employee_id = models.CharField(max_length=7, unique=True, editable=False)
    department = models.CharField(max_length=50, choices=Department.choices)
    position = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        MAX_ATTEMPTS = 3
        attempt = 0

        while attempt < MAX_ATTEMPTS:
            if not self.employee_id:
                self.employee_id = generate_employee_id(self.department)
            try:
                with transaction.atomic():
                    super().save(*args, **kwargs)
                return  # success
            except IntegrityError:
                # Retry with a new ID
                attempt += 1
                self.employee_id = None

        # If all attempts fail
        raise IntegrityError("Could not generate unique employee ID after 3 attempts.")

    def __str__(self):
        return f"{self.user.username} ({self.employee_id})"


class AttendanceRecord(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=AttendanceStatus.choices,
        default=AttendanceStatus.ABSENT
    )
    marked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='marked_attendance')
    note = models.TextField(blank=True)

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee.employee_id} - {self.date} ({self.status})"
