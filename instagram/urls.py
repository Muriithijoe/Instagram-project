from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.post,name = 'post'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^profile/',views.profile,name = 'Profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
