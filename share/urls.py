from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^signup/', views.signup, name = 'signup'),
    url(r'^updateProfile/', views.updateProfile, name = 'update'),
    url(r'^profile/(?P<regNum>[^/]+)/$',views.profile,name='profile'),
    url(r'^signout/', views.signout, name = 'logout'),
]