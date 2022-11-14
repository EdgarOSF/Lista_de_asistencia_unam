from django.urls import path
from .views import upload_file_list_view


urlpatterns = [
    path('', upload_file_list_view, name='form_file_list')
]
