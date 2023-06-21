from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path as url
from first_app import views
from django.contrib.auth import views as auth_views


app_name = 'first_app'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('admin/', admin.site.urls),
    # AUTH
    url('signup', views.SignUp.as_view(), name='signup'),
    url('login', auth_views.LoginView.as_view(), name='login'),
    url('logout', auth_views.LogoutView.as_view(), name='logout'),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
