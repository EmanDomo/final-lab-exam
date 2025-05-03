from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, ProductViewSet, AddToCartView, RegisterView
from rest_framework.routers import DefaultRouter
from django.conf import settings  # Fixed typo here (was 'rom')
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    # Custom token view to include role in JWT
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Token refresh
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Other paths
    path('register/', RegisterView.as_view()),
    path('checkout/', AddToCartView.as_view()),
]

# Merge router URLs with the custom paths
urlpatterns += router.urls

# Add media serving in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)