
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
    # path('stuinfo/<int:pk>',views.student_list),
    # path('stuinfo/',views.student_details),
]
