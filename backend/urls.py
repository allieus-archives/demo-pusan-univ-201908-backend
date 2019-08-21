from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('univ/', include('univ.urls')),
    re_path('', TemplateView.as_view(template_name='root.html')),
]
