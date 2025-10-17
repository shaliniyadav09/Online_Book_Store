from django.urls import path 
from . import views
urlpatterns = [
    
    path('admindash/',views.admindash, name='admindash'),
    path('adminlogout/',views.adminlogout, name='adminlogout'),
    path('viewenqs/',views.viewenqs, name='viewenqs'),
    path('delenqs/<id>',views.delenqs, name='delenqs'),
    path('addcat/',views.addcat, name='addcat'),
    path('viewcat/',views.viewcat, name='viewcat'),
    path('delviewcat/<id>',views.delviewcat, name='delviewcat'),
    path('addbook/',views.addbook, name='addbook'),
    path('viewbook/',views.viewbook, name='viewbook'),
    path('delbook/<id>',views.delbook, name='delbook'),
    path('editbook/<id>',views.editbook, name='editbook'),
    

 






















 
    
]
 