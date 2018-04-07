from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^signup/', views.signup, name = 'signup'),
    url(r'^login/',views.signin,name = 'login'),
    url(r'^updateProfile/', views.updateProfile, name = 'update'),
    url(r'^profile/(?P<regNum>[^/]+)/$',views.profile,name='profile'),
    url(r'^signout/', views.signout, name = 'logout'),
    url(r'^manage$', views.manage, name = 'manage'),
    url(r'^manage/add$', views.addItem, name = 'additem'),
    # url(r'^discover/$', views.discover, name = 'discover'),
    url(r'^search$', views.search, name = 'search'),
]