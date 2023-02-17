from django.contrib import admin
from django.urls import path, include
import gukbab.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gukbab.views.index, name='index'),
    path('gukbab/', include('gukbab.urls')),
]
