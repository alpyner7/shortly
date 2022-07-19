from django.contrib import admin
from django.urls import path
from authentication.views import home, login, signup, logout
from urlhandler.views import dashboard, generate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('login', login, name = 'login'),
    path('signup', signup, name = 'signup'),
    path('logout', logout, name = 'logout'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('generate', generate, name = 'generate'),
]