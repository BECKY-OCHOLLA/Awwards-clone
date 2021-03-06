from django.conf.urls import url
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('update/<id>', views.update_profile, name='update_profile'),
    path('post/',views.post_project,name='post_project'),
    path('project/(<id>', views.view_project, name='view_project'),
    path('api/v1/profile',views.ProfileList.as_view(),name='profileEndpoint'),
    path('api/v1/projects',views.ProjectList.as_view(),name='projectsEndpoint')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)