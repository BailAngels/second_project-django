from django.urls import path

from apps.tags import views


urlpatterns = [
    path('tags/', views.TagListView.as_view(), name='tagslist'),
    path('tag_create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag_update/<int:pk>/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tag_detail/<int:pk>/', views.TagRetrieveView.as_view(), name='tag_detail'),
    path('tag_delete/<int:pk>/', views.TagDestroyView.as_view(), name='tag_delete'),
]
