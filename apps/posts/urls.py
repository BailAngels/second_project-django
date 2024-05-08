from django.urls import path

from apps.posts import views


urlpatterns = [
    path('',views.PostListView.as_view(),name='index'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.PostRetrieveView.as_view(),name = 'detail'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(),name = 'update'),
    path('delete/<int:pk>/', views.PostDestroyView.as_view(),name = 'delete'),
]

