from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupChatViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'groupchats', GroupChatViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
