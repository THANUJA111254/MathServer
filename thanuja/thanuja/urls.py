from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('power_calculator/',views.power_calculator,name='power_calculator'),
    path('',views.power_calculator,name="power_calculator")
]