from django.shortcuts import render,HttpResponse
from django.http import HttpResponseForbidden
from django.db import IntegrityError
# from registration_app import models
from registration_app.models import Registration
import re

# Create your views here.
def url_redirect(request):
    return render(request,"index.html", {'duplicate_email': False})

#this is helping function for name vaildation
def contains_alphabets(input_string):
    cleaned_string = input_string.replace(' ', '_')
    # Remove special characters and numbers
    cleaned_string = re.sub(r'[^a-zA-Z_]', '', cleaned_string)

    # Check if the cleaned string contains alphabets
    return any(char.isalpha() for char in cleaned_string),cleaned_string

def add_registration(request):
    if request.method == 'POST':
        form_data = request.POST.dict()
        full_name_from_req=form_data.get('full_name', '')
        email_from_req=form_data.get('email', '')
        gender_from_req=form_data.get('gender', '')
        course_from_req=form_data.get('course', '')
        department_from_req=form_data.get('department', '')
        college_name_from_req=form_data.get('college_name', '')
       # verify that the name is corrected or not!
        if full_name_from_req !="":
            result,new_name=contains_alphabets(full_name_from_req)
            if result:
                full_name_from_req=new_name
            else:
                return render(request,"failure.html")
        if full_name_from_req =="" or email_from_req=="" or gender_from_req=="" or course_from_req=="" or department_from_req=="" or college_name_from_req =="":
            return render(request,"failure.html") 
       
        # Create or get a Registration instance
        try:
            new_registration, created = Registration.objects.get_or_create(
                email=email_from_req,
                defaults={
                    'full_name': full_name_from_req,
                    'gender': gender_from_req,
                    'course': course_from_req,
                    'department': department_from_req,
                    'college_name': college_name_from_req,
                    # Add other fields similarly
                }
            )
       
            if created:
                return render(request,"success.html")
            else:
                return render(request,"index.html", {'duplicate_email': True})

        except Exception as e:
            return render(request, "failure.html")

    return render(request,"failure.html") 