from django.urls import path
from fly import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('registration/',views.registration,name='registration'),
    path('bookticket/mybooking/',views.mybooking,name='mybooking'),
    path('selectflight/',views.selectflight,name='selectflight'),
    path('confirmbooking/',views.confirmbooking,name='confirmbooking'),
    path('bookticket/',views.bookticket,name='bookticket'),
] 

