from .views import PetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('pets', PetViewSet, basename='pet')

urlpatterns = router.urls
