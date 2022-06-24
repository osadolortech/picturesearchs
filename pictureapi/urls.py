from rest_framework import routers
from .views import PictureView

router = routers.DefaultRouter()
router.register('images', PictureView)