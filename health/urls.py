from django.urls import path
from.import views
urlpatterns = [
    path('',views.health, name='health'),
    path('appointment/',views.appointment, name='appointment')
]