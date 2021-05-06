from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    driver_name=models.CharField(max_length=150)
    mobile_no=models.CharField(max_length=20, null=True)
    pin_code=models.CharField(max_length=10, null=True)
    mohalla_or_village=models.CharField(max_length=200, null=True)
    district=models.CharField(max_length=200, null=True)
    state=models.CharField(max_length=200, null=True)
    vehicle_registration_no=models.CharField(max_length=100, null=True)
    vehicle_brand=models.CharField(max_length=100, null=True)
    vehicle_model=models.CharField(max_length=100, null=True)
    insurance_validity=models.CharField(max_length=100, null=True)
    insurance_type=models.CharField(max_length=100, null=True)
    registration_year=models.CharField(max_length=10, null=True)
    km_driven=models.CharField(max_length=50, null=True)
    choice=(('UNDER VARIFICATION','UNDER VARIFICATION'),('ACTIVE','ACTIVE'),('OFFLINE','OFFLINE'),('ON A RIDE','ON A RIDE'))
    status=models.CharField(max_length=50, choices=choice, default='pending', null=True) 


    def __str__(self):
        return self.driver_name

class CustomerUser(models.Model):
    user_name=models.CharField(max_length=150, null=True)
    mobile_no=models.CharField(max_length=25, null=True)
    wallet_amount=models.CharField(max_length=10, null=True)
    email_id=models.EmailField(max_length=60, null=True, blank=True)
    User_Id=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user_name


class Vehicle(models.Model):
    brand=models.CharField(max_length=150)
    model=models.CharField(max_length=150)
    fare_per_km=models.IntegerField()
    air_conditioned=models.BooleanField()
    luggage_capacity=models.IntegerField()
    number_of_seat=models.IntegerField()
    front_image=models.ImageField(upload_to="Vehicles",null=True, blank=True)
    side_image=models.ImageField(upload_to="Vehicles",null=True, blank=True)
    back_image=models.ImageField(upload_to="Vehicles",null=True, blank=True)

    def __str__(self):
        return self.brand

class BookingHistory(models.Model):
    booking_id=models.AutoField()
    booking_Date=models.CharField(max_length=50, unique=True)
    choice=(('Round trip','Round trip'),('One way','One way'),('Local','Local'))
    trip_type=models.CharField(max_length=50, choices=choice, default='', null=True) 
    pickup_date_time=models.CharField(max_length=70)
    drop_date=models.CharField(max_length=70)
    km_travelled=models.CharField(max_length=50)
    pickup_point=models.CharField(max_length=150)
    drop_point=models.CharField(max_length=150)
    booked_by_user=models.CharField(max_length=20)
    assigned_driver=models.CharField(max_length=20)
    booked_vehicle=models.CharField(max_length=150)

    def __str__(self):
        return self.booking_id

class Admin(models.Model):
    name=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=25)
    email=models.EmailField(max_length=60, null=True, blank=True)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name  


class BookingDetails(models.Model):
    choice=(('Round trip','Round trip'),('One way','One way'),('Local','Local'))
    trip_type=models.CharField(max_length=50, choices=choice, default='', null=True) 
    pickup_point=models.CharField(max_length=150)
    Pickup_date_time=models.CharField(max_length=70)
    drop_point=models.CharField(max_length=150)
    drop_date=models.CharField(max_length=70)
    selected_car=models.CharField(max_length=150)
    name =models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=25)
    user_id=models.AutoField()
    approx_km_travelling=models.CharField(max_length=50)
    coupon=models.CharField(max_length=150)
    coupon_discount_amount =models.CharField(max_length=50)
    fare=models.CharField(max_length=50)
    advance_payment_medium=models.CharField(max_length=50)
    cash_drop_point=models.CharField(max_length=150,null=True,black=True) 
    transaction_no=models.CharField(max_length=100,null=True,black=True) 

    def __str__(self):
        return self.trip_type 