from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from app.models import *

class DriverSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Driver
        fields=['driver_id','driver_name','mobile_no','pin_code','mohalla_or_village','district','state','vehicle_registration_no','vehicle_brand','vehicle_model','insurance_validity','insurance_type','registration_year','km_driven','status']

class CustomerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=CustomerUser
        fields=['User_Id','user_name','mobile_no','wallet_amount','email_id']

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model=Vehicle
        fields=['vehicle_id','brand','model','fare_per_km','air_conditioned','luggage_capacity','number_of_seat','front_image','side_image','back_image']
                                                                

class BookingDetailsSerializer(serializers.ModelSerializer):
    assign_driver = DriverSerializer(read_only=True)
    class Meta:
        model=BookingDetails
        fields=['booking_id','trip_type','pickup_point','Pickup_date_time','drop_point','drop_date','selected_car','name','mobile_no','user_id','approx_km_travelling','coupon','coupon_discount_amount','fare','advance_payment_medium','cash_drop_point','transaction_no','assign_driver']                                                                                                                            

class BookingHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model=BookingHistory
        fields=['booking_history_id','trip_type','booking_Date','pickup_date_time','drop_date','km_travelled','pickup_point','drop_point','booked_by_user','assigned_driver','booked_vehicle']


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Notification
        fields=['id','title','description','type']

class CouponsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Coupons
        fields=['id','coupon']