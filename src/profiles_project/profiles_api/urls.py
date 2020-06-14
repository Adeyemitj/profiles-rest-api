from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views
from . import models

# create a variable and assigned DefaultRouter() function to it
router = DefaultRouter()
# Register your new URL that point to the router
router.register('hello-viewset', views.Helloviewset, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    url(r'^hello-view/', views.HelloView.as_view()),
    url(r'', include(router.urls)),

]
