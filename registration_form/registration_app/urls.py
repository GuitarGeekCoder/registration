
from django.contrib import admin
from django.urls import path
from registration_app import views
app_name = 'register_ME'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.url_redirect,name="registration"),
    path('register_ME/',views.add_registration,name="register_ME")
]
