from django.urls import path
from . import views

# this is like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    # Read/View index route
    path('pierogi/', views.AllPierogi.as_view(), name='all_pierogi'),
    # Read/View detail route
    path('pierogi/<int:pk>', views.PierogiDetail.as_view(), name='pierogi_detail'),
    # Create/Add route
    path('pierogi/new', views.PierogiCreate.as_view(), name='pierogi_create'),
    # Update/Edit route
    path('pierogi/<int:pk>/edit', views.PierogiUpdate.as_view(), name='pierogi_edit'),
    # Destroy/Delete route
    path('pierogi/<int:pk>/delete', views.PierogiDelete.as_view(), name='pierogi_delete'),
]