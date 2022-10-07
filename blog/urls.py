from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from kama import settings

urlpatterns = [
    path('', views.index, name="index" ),
    re_path(r'^detail_produit/(?P<produit_id>[0-9]+)$', views.detail_produit, name='detail_produit'),
    path('recherche_forms/', views.recherche_forms, name='recherche_forms'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
