from rest_framework import routers

from applications.twits.views import FilmViewSet, ReviewViewSet, CommentViewSet
router = routers.DefaultRouter()
router.register(r'film', FilmViewSet, basename='film')
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'comment', CommentViewSet, basename='comment')
urlpatterns = router.urls
