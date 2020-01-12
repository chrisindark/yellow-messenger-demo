from django.urls import path
from tinyurls import views


urlpatterns = [
    path('tinyurls/', views.TinyUrlListCreateApiView.as_view()),
    path('tinyurls/<slug:tiny_id>/', views.TinyUrlDetailApiView.as_view()),
]
