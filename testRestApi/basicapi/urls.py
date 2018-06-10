
from django.conf.urls import url, include
from rest_framework import routers

#from bbs import views as bbs_views
from basicapi import views as rest_views

#for the uploading the file
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)
#router.register(r'groups', rest_views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
#    url(r'^(?p<pk>[0-9]+)/$', rest_views.UserViewSet),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    url(r'fish', rest_views.fish),
    url(r'fish', rest_views.FishAnalysisView.as_view(), name='file-upload'),
    url(r'report', rest_views.ReportView.as_view(), name='bug-report'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

