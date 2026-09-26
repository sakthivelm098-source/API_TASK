from django.db import models


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.departmentName


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.fullName