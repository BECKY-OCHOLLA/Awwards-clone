from django.conf.urls import url
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('update/<id>', views.update_profile, name='update_profile'),
    path('post/',views.post_project,name='post_project'),
    path('project/(<id>', views.view_project, name='view_project'),

]
    