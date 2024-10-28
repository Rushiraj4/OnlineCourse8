from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from onlinecourse.views import CourseListView  # Import the view if it's in the onlinecourse app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onlinecourse/', include('onlinecourse.urls')),
    path('', CourseListView.as_view(), name='home'),  # Direct root URL to the course list
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
