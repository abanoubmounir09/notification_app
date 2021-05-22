
from django.contrib import admin
from django.urls import path,include
from notifyApp import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name='index'),
    path('message', views.message, name='message'),
    path('multimessages', views.multimessage, name='multimessage'),
    path('notifications', views.get_notify, name='get_notify'),
    path('mark_read_message/<int:id>/', views.mark_message_read, name='readMessage'),
    path('register',views.register,name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('user/', views.current_user, name='current_user'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
