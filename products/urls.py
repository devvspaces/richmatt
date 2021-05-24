from django.urls import path
from .views import *

urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('store/', ProductsView.as_view(), name='products'),
	path('manage/store/', ManageProduct.as_view(), name='manage_product'),
	path('manage/store/add/', AddProduct.as_view(), name='add_product'),
	path('manage/store/update/<int:id>/', UpdateProduct.as_view(), name='update_product'),
	path('manage/store/delete/<int:id>/', DeleteProduct.as_view(), name='delete_product'),
]
