from django.contrib import admin
from django.urls import path, include
from entries.views import CookieTokenRefreshView, LogoutView, MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('entries.urls')),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', CookieTokenRefreshView.as_view(), name='login_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api-auth/', include('rest_framework.urls')),
]
