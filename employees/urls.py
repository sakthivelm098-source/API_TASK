from django.urls import path

from . import views


urlpatterns = [

    # =========================
    # LOCATIONS
    # =========================

    path(
        "locations/",
        views.location_list,
        name="location_list"
    ),

    path(
        "locations/<int:id>/",
        views.location_detail,
        name="location_detail"
    ),


    # =========================
    # DEPARTMENTS
    # =========================

    path(
        "departments/",
        views.department_list,
        name="department_list"
    ),

    path(
        "departments/<int:id>/",
        views.department_detail,
        name="department_detail"
    ),


    # =========================
    # EMPLOYEES
    # =========================

    path(
        "employees/",
        views.employee_list,
        name="employee_list"
    ),

    path(
        "employees/<int:id>/",
        views.employee_detail,
        name="employee_detail"
    ),


    # =========================
    # FULL EMPLOYEE DETAILS
    # =========================

    path(
        "employee-details/",
        views.employee_full_details,
        name="employee_full_details"
    ),

    path(
        "employee-details/<int:id>/",
        views.employee_full_detail_by_id,
        name="employee_full_detail_by_id"
    ),
]