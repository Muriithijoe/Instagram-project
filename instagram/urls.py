from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^post',views.post, name = 'post'),
    url(r'^new-post',views.new_post, name = 'new-post'),
    url(r'^profile/',views.profile,name = 'Profile'),
    url(r'^edit-profile/',views.edit_profile,name = 'edit-profile'),
    url(r'^search_profile/(\d+)',views.search_profile,name = 'search_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
