from django.urls import path, include
from .views import *

urlpatterns = [
    path('get-jobs/', GetJobs.as_view()),
]
