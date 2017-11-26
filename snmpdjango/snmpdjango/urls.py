from django.conf.urls import url, include
from django.contrib import admin
# from core.views import informacoes


urlpatterns = [
    url(r'^', include('core.urls')),
    # url(r'^informacoes/$', informacoes, name='core_informacoes'),
    url(r'^admin/', admin.site.urls),
]
