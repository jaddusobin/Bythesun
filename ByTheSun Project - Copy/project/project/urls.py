"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index),
    path('customerreg/',views.customerreg),
    path('servicecenterreg/',views.service_centerreg),
    path('login/',views.login),
    path('adminhome/',views.adminhome),
    path('customerhome/',views.customerhome),
    path('servicecenterhome/',views.service_centerhome),
    path('viewcustomers/',views.viewcustomers),
    path('actioncustomers/',views.actioncustomers),
    path('rejectcustomers/',views.rejectcustomers),
    path('deletecustomers/',views.deletecustomers),
    path('viewcenters/',views.viewservice_center),
    path('actioncenters/',views.actioncenters),
    path('rejectcenters/',views.rejectcenters),
    path('deletecenters/',views.deletecenters),
    path('addproducts/',views.addsolar_products),
    path('viewproducts/',views.viewproducts),
    path('editproducts/',views.editproducts),
    path('viewsolarproducts/',views.viewsolar_products),
    path('viewproduct_detail/',views.viewproduct_detail),
    path('viewcart/',views.viewcart),
    path('deletecart/',views.deletecart),
    path('addpayment/',views.addpayment),
    path('vieworder/',views.vieworder),
    path('viewitems/',views.viewitems),
    path('vieworder_ad/',views.vieworder_ad),
    path('addfeedback/',views.addfeedback),
    path('viewfeedback/',views.viewfeedback),
    path('addreply/',views.addreply),
    path('viewcenter/',views.viewservice_centers),
    path('bookcenter/',views.bookcenter),
    path('viewbooking/',views.viewbooking),
    path('actionbooking/',views.actionbooking),
    path('rejectbooking/',views.rejectbooking),
    path('viewbooking_se/',views.viewbooking_se),
    path('payment/',views.payment),
    path('viewpayment/',views.viewpayment),
    path('addrequest/',views.addrequest),
    path('viewrequest/',views.viewrequest),
    path('actionrequest/',views.actionrequest),
    path('rejectrequest/',views.rejectrequest),
    path('viewselling/',views.viewselling),
]
