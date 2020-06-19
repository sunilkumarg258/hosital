from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('register/', views.register1, name='register'),
    path('login/', views.login1, name='login'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('About/', views.aboutus, name='About'),
    path('Departments/', views.departments, name='Departments'),
    path('Doctors/', views.doctors, name='Doctors'),
    path('Blog_home/', views.blog_home, name='Blog_home'),
    path('Blog_details/', views.blog_details, name='Blog_details'),
    path('Contact/', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('appointment/', views.appointment, name='appointment')
]
