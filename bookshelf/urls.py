from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet, BookInfoView, BookUpdateView , BookDeleteView ,UserListView ,BookDetailView

router = DefaultRouter()

router.register(r'signup', UserViewSet)
# router.register(r'books', BookViewSet)
router.register(r'books', BookDetailView)


urlpatterns = [
    path('', include((router.urls))),
    path('myself/',UserListView.as_view(),name='myself'),
    path('book-info/<int:isbn>/', BookInfoView.as_view(), name='book-info'),
    path('books/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),



]
