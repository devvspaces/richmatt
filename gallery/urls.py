from django.urls import path
from .views import *

urlpatterns = [
	path('', GalleryView.as_view(), name='gallery'),
	path('manage/', ManageGallery.as_view(), name='manage_gallery'),
	path('manage/add/', AddGallery.as_view(), name='add_gallery'),
	path('manage/update/<int:id>/', UpdateGallery.as_view(), name='update_gallery'),
	path('manage/delete/<int:id>/', DeleteGallery.as_view(), name='delete_gallery'),
]