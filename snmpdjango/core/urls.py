from django.conf.urls import url
from core.views import home, informacoes

urlpatterns = [
    url(r'^$', home),
    url(r'^informacoes/$', informacoes),

]
 