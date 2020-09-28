from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("/courses", views.courses, name='courses'),
    url(r'^/courses/(?P<pk>\d+)/$', views.cour_desc, name='cour_desc'),
    path("home/contactus", views.contactus, name="contactus"),
    url(r'^/(?P<pk>\d+)/pay/$', views.initiate_payment, name='pay'),
    path('callback/', views.callback, name='callback'),
    path("/course/pay/verification", views.verification, name='verification'),
    path("/course/pay/verification/enrolled", views.enrolled, name="enrolled"),
    path("home/preview", views.preview, name="Preview"),
    path("home/howweteach", views.howweteach, name="howweteach")
]
