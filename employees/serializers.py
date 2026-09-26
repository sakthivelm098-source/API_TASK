from rest_framework import serializers

from .models import Employee, Department, Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = [
            "location_id",
            "city"
        ]


class DepartmentSerializer(serializers.ModelSerializer):

    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source="location"
    )

    class Meta:
        model = Department
        fields = [
            "department_id",
            "departmentName",
            "location_id"
        ]


class EmployeeSerializer(serializers.ModelSerializer):

    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source="department"
    )

    class Meta:
        model = Employee
        fields = [
            "employee_id",
            "fullName",
            "salary",
            "department_id"
        ]


class EmployeeDetailSerializer(serializers.ModelSerializer):

    department_id = serializers.IntegerField(
        source="department.department_id"
    )

    Department_id = serializers.IntegerField(
        source="department.department_id"
    )

    departmentName = serializers.CharField(
        source="department.departmentName"
    )

    location_id = serializers.IntegerField(
        source="department.location.location_id"
    )

    Location_id = serializers.IntegerField(
        source="department.location.location_id"
    )

    city = serializers.CharField(
        source="department.location.city"
    )

    class Meta:
        model = Employee

        fields = [
            "employee_id",
            "fullName",
            "salary",
            "department_id",
            "Department_id",
            "departmentName",
            "location_id",
            "Location_id",
            "city"
        ]