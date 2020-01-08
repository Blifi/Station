
from django.contrib import admin  
from django.urls import path  
from employee import views
from station import views  as stationViews  
from employee.views import ToDoViews

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('empapi', views.empapi), 
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
    path('todo/api/', ToDoViews.as_view()),
    path('station', stationViews.station),
    path('data', stationViews.data),  
    path('datashow', stationViews.datashow),    
]  