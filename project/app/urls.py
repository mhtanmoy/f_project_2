from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('driver', views.driver, name='driver'),
    path('editdriver/<int:pk>', views.editdriver, name='editdriver'),
    path('edituser/<int:pk>', views.edituser, name='edituser'),
    path('vehicle', views.vehicle),
    path('bookinghistory', views.bookinghistory),
    path('bookingdetails', views.bookingdetails),
    path('customeruser', views.customeruser, name='customeruser'),
    path('users', views.alluser),
    path('signup', views.signupuser, name='signupuser'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),

]