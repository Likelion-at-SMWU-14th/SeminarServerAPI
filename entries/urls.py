from rest_framework.routers import DefaultRouter
from .views import EntryViewSet

router = DefaultRouter()
router.register(r'entries', EntryViewSet)

urlpatterns = router.urls