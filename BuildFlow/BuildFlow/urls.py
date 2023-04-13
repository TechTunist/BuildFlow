from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include(('DataFlow.urls', 'dataflow'), namespace='dataflow')),
    path('authenticate/', include(('AuthFlow.urls', 'authflow'), namespace='authflow')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

