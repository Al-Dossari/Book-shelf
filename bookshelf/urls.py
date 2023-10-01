from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet, BookInfoView, BookUpdateView , BookDeleteView ,UserView

router = DefaultRouter()

router.register(r'signup', UserViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include((router.urls))),
    path('myself/',UserView.as_view(),name='myself'),
    path('book-info/<str:isbn>/', BookInfoView.as_view(), name='book-info'),
    path('books/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete')

]
