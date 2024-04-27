from django.urls import path
from login.views import *
urlpatterns=[
		path('customersignup/', CustomerSignup.as_view(), name='customersignup'),
        path('adminsignup/',AdminSignup.as_view(), name='adminsignup'),
        
		# path('login/', Login.as_view(), name='login'),
    	path('test/view/', TestView.as_view(), name='test_view'),
    	path('logout/', Logout.as_view(), name='logout'),
        
		path('category/list',category_list,name='category_list'),
         path('category/add',category_add,name='category_add'),

]
