from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    UsersViewSet,
    EmailConfirm,
    GenresModelViewSet,
    TitlesModelViewSet,
    CategoryModelViewSet,
    ReviewViewSet,
    CommentViewSet
)

router_v1 = DefaultRouter()
router_v1.register('users', UsersViewSet, basename='users')
router_v1.register('auth', EmailConfirm, basename='emailconfirm')
router_v1.register('categories', CategoryModelViewSet, basename='categories')
router_v1.register('genres', GenresModelViewSet, basename="genres")
router_v1.register('titles', TitlesModelViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review',
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
