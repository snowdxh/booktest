from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('', views.BookView.as_view(),name='books')
]


router = DefaultRouter()
router.register('book', views.BookView)
urlpatterns += router.urls


