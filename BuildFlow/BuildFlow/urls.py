from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include(('DataFlow.urls', 'dataflow'), namespace='dataflow')),
    path('authenticate/', include(('AuthFlow.urls', 'authflow'), namespace='authflow')),
    
]
