from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('react/', TemplateView.as_view(template_name='index.html')),
    path('api/', include('notesapi.urls')),
    path('api2/', include('api.urls'))
]
