from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CategoryViewSet, AttachmentViewSet, ReportViewSet # type: ignore

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'attachments', AttachmentViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
