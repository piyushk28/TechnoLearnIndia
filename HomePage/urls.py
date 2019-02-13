from django.urls import path
from .views import home_view

app_name='HomePage'
urlpatterns = [
    path('<pk>/', home_view,name='home'),
]