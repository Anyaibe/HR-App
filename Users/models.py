import uuid
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager

class Department(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()
    employee_count = models.IntegerField()

    def __str__(self):
        return self.name

user_type = [
    ("Applicant", "Applicant"),
    ("Contract", "Contract"),
    ("Staff", "Staff"),
    ("Admin", "Admin")
]


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=15)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="User_profile", null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    account_status = models.CharField(max_length=20, choices=[("Active", "Active"), ("Blocked", "Blocked"),
                                                              ("Admin", "Admin"), ("Leave", "Leave"), ("Training", "Training")], default="Active")
    account_type = models.CharField(max_length=20, choices=user_type, default="")
    password_updated = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'phone']
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_username(self):
        return f"{self.firstname} {self.lastname}"

    def delete(self, *args, **kwargs):
        if self.is_staff:
            self.is_active = False
            self.account_status = 'Blocked'
            self.save(update_fields=['is_active', 'account_status'])
        else:
            super().delete(*args, **kwargs)

gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Rather_Not_Say", "Rather Not Say")
)

marital_status = (
    ("Single", "Single"),
    ("Married", "Married"),
    ("Divorced", "Divorced")
)

class StaffBioData(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="bio_data")
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=20, choices=gender)
    marital_status = models.CharField(max_length=10, choices=marital_status)
    nationality = models.CharField(max_length=25)
    Address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="Nigeria")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_username()
    
employment_type = (
    ("FullTime", "Full time"),
    ("PartTime", "Part Time"),
    ("Contract", "Contract")
)


class StaffProfessionalData(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="professional_data")
    employment_type = models.CharField(max_length=15, choices=employment_type)
    company_email = models.EmailField(unique=True)
    contract_length = models.CharField(max_length=25)
    department = models.ForeignKey("users.Department", on_delete=models.SET_NULL, null=True, blank=True)
    sector = models.ForeignKey("users.StaffSector", on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    working_days = models.CharField(max_length=50)
    working_hours = models.CharField(max_length=25)
    join_date = models.DateField()
    office_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_username()
    

leave_type = [
    ("SickLeave", "Sick Leave"),
    ("AnnualLeave", "Annual Leave"),
    ("CompassionateLeave", "Compassionate Leave"),
    ("Other", "Other")
]

leave_status = [
    ("Pending", "Pending"),
    ("Cancelled", "Cancelled"),
    ("Rejected", "Rejected"),
    ("Approved", "Approved"),
    ("Active", "Active"),
    ("Completed", "Completed")
]


class LeaveApplication(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="requester")
    approved_by = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_by")
    type = models.CharField(max_length=25, choices=leave_type)
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=leave_status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_username()

# Create your models here.
