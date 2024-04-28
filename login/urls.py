from django.urls import path
from login.views import *
urlpatterns=[
    
		path('customersignup/', CustomerSignup.as_view(), name='customersignup'),
        path('adminsignup/', AdminSignup.as_view(), name='adminsignup'),
        path('salersignup/', SalerSignup.as_view(), name='salersignup'),
        
		# path('login/', Login.as_view(), name='login'),
    	path('test/view/', TestView.as_view(), name='test_view'),
    	path('logout/', Logout.as_view(), name='logout'),

]
