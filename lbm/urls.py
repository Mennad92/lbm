from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from biscuits import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'profile', views.ProfileViewSet, basename='profile')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', views.EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)