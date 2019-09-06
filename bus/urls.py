from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^category/(\d+)',views.category_filter,name = 'category'),
    url(r'^hire/$',views.car,name = 'car'),
    url(r'^car/$',views.view_car,name = 'view_car'),
    url(r'comment/$', views.comment, name='comment'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
