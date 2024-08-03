from django.contrib import admin
from django.urls import path
from challenges import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('stage_one/', views.stage_one, name='stage_one'),
    path('stage_two/', views.stage_two, name='stage_two'),
    path('stage_three/', views.stage_three, name='stage_three'),
    path('stage_four/', views.stage_four, name='stage_four'),
    path('stage_five/', views.stage_five, name='stage_five'),
    path('stage_six/', views.stage_six, name='stage_six'),
    path('stage_seven/', views.stage_seven, name='stage_seven'),
    path('stage_eight/', views.stage_eight, name='stage_eight'),
]
