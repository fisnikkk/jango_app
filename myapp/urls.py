from django.urls import path
from . import views
from myapp.streamlit_view import app as streamlit_app

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('about/', views.about, name='about'),
    path('streamlit/', streamlit_app, name='streamlit'),
]
