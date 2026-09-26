from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Employee, Department, Location

from .serializers import (
    EmployeeSerializer,
    DepartmentSerializer,
    LocationSerializer,
    EmployeeDetailSerializer
)


# =========================================================
# LOCATION
# =========================================================

@api_view(["GET", "POST"])
def location_list(request):

    # GET ALL LOCATIONS
    if request.method == "GET":

        locations = Location.objects.all()

        serializer = LocationSerializer(
            locations,
            many=True
        )

        return Response(serializer.data)

    # CREATE LOCATION
    if request.method == "POST":

        serializer = LocationSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def location_detail(request, id):

    try:

        location = Location.objects.get(
            location_id=id
        )

    except Location.DoesNotExist:

        return Response(
            {"error": "Location not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET BY ID
    if request.method == "GET":

        serializer = LocationSerializer(location)

        return Response(serializer.data)

    # UPDATE
    if request.method == "PUT":

        serializer = LocationSerializer(
            location,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE
    if request.method == "DELETE":

        location.delete()

        return Response(
            {
                "message": "Location deleted successfully"
            },
            status=status.HTTP_200_OK
        )


# =========================================================
# DEPARTMENT
# =========================================================

@api_view(["GET", "POST"])
def department_list(request):

    # GET ALL DEPARTMENTS
    if request.method == "GET":

        departments = Department.objects.all()

        serializer = DepartmentSerializer(
            departments,
            many=True
        )

        return Response(serializer.data)

    # CREATE DEPARTMENT
    if request.method == "POST":

        serializer = DepartmentSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def department_detail(request, id):

    try:

        department = Department.objects.get(
            department_id=id
        )

    except Department.DoesNotExist:

        return Response(
            {"error": "Department not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET BY ID
    if request.method == "GET":

        serializer = DepartmentSerializer(
            department
        )

        return Response(serializer.data)

    # UPDATE
    if request.method == "PUT":

        serializer = DepartmentSerializer(
            department,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE
    if request.method == "DELETE":

        # Delete employees belonging to this department
        Employee.objects.filter(
            department=department
        ).delete()

        # Delete department
        department.delete()

        return Response(
            {
                "message": "Department deleted successfully"
            },
            status=status.HTTP_200_OK
        )


# =========================================================
# EMPLOYEE
# =========================================================

@api_view(["GET", "POST"])
def employee_list(request):

    # GET ALL EMPLOYEES
    if request.method == "GET":

        employees = Employee.objects.all()

        # Salary filter
        salary = request.query_params.get("salary")

        if salary:

            employees = employees.filter(
                salary__gte=salary
            )

        serializer = EmployeeSerializer(
            employees,
            many=True
        )

        return Response(serializer.data)

    # CREATE EMPLOYEE
    if request.method == "POST":

        serializer = EmployeeSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def employee_detail(request, id):

    try:

        employee = Employee.objects.get(
            employee_id=id
        )

    except Employee.DoesNotExist:

        return Response(
            {
                "error": "Employee not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    # GET BY ID
    if request.method == "GET":

        serializer = EmployeeSerializer(
            employee
        )

        return Response(serializer.data)

    # UPDATE
    if request.method == "PUT":

        serializer = EmployeeSerializer(
            employee,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE
    if request.method == "DELETE":

        employee.delete()

        return Response(
            {
                "message": "Employee deleted successfully"
            },
            status=status.HTTP_200_OK
        )


# =========================================================
# FULL EMPLOYEE DETAILS
# =========================================================

@api_view(["GET"])
def employee_full_details(request):

    employees = Employee.objects.select_related(
        "department",
        "department__location"
    )

    # Department filter
    department_id = request.query_params.get(
        "department_id"
    )

    if department_id:

        employees = employees.filter(
            department__department_id=department_id
        )

    # Location filter
    location_id = request.query_params.get(
        "location_id"
    )

    if location_id:

        employees = employees.filter(
            department__location__location_id=location_id
        )

    serializer = EmployeeDetailSerializer(
        employees,
        many=True
    )

    return Response(serializer.data)


# =========================================================
# FULL EMPLOYEE DETAILS BY ID
# =========================================================

@api_view(["GET"])
def employee_full_detail_by_id(request, id):

    try:

        employee = Employee.objects.select_related(
            "department",
            "department__location"
        ).get(
            employee_id=id
        )

    except Employee.DoesNotExist:

        return Response(
            {
                "error": "Employee not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = EmployeeDetailSerializer(
        employee
    )

    return Response(serializer.data)