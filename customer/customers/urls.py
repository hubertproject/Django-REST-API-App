from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerList.as_view()),
    path('<int:pk>', views.CustomerDetails.as_view())

]
