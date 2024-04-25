from django.urls import path
from login.views import *
urlpatterns=[
		path('signup/', Signup.as_view(), name='signup'),
		path('login/', Login.as_view(), name='login'),
    	path('test/view/', TestView.as_view(), name='test_view'),
    	path('logout/', Logout.as_view(), name='logout')

]
