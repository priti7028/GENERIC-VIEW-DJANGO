from django.urls import path
from . views import Create_View,List_View,Update_View,Delete_View,Detail_View

urlpatterns=[
    path('cv/',Create_View.as_view(),name='create_url'),
    path('lv/',List_View.as_view(),name='list_url'),
    path('uv/<int:pk>/',Update_View.as_view(),name='update_url'),
    path('dv/<pk>/',Delete_View.as_view(),name='delete_url'),
    path('de/<int:pk>/',Detail_View.as_view(),name='details_url')
]
