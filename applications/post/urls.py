from django.urls import path, include
from applications.post.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('image', ImageModelViewSet)
router.register('comment', CommentModelViewSet)
router.register('', ShoesAPIView)
# router.register('category', CategoryAPIView)


urlpatterns = [

]

urlpatterns += router.urls
