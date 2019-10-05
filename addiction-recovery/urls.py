from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('jet/', include('jet.urls', 'jet')),  
    path('admin/',admin.site.urls),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
   
]
