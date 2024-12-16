from . views import *
from django.urls import path

from . views import *
urlpatterns = [
    path('',home,name='home'),
    path('course/<int:course_id>/', posts_by_category, name='posts_by_category'),
    path('student/<int:student_id>/', post_detail, name='post_detail'),
]
