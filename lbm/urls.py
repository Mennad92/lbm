from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from biscuits import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('dj/', include('dj_rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
