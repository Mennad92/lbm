from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from biscuits import views

router = routers.DefaultRouter()
router.register(r'produits', views.ProduitViewSet)
router.register(r'categories', views.CategorieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
