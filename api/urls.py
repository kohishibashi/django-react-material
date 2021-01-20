from django.urls import path, include
# from rest_framework import routers
from api.views import PostViewSet, PostListView, PostDetailView

# router = routers.DefaultRouter()
# router.register('posts', PostViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('posts/', PostViewSet.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('posts/', PostListView.as_view()),
]