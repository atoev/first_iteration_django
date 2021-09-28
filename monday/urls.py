from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include(('landing.urls', 'landing'), namespace='landing'))
]
urlpatterns += staticfiles_urlpatterns()
