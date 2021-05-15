from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
        path('', views.post_list, name='post_list'),
        path('<id>/', views.post_detail, name='post_detail' ),
        path('tags/<tag>/', views.post_by_tag, name='post_by_tag' ),
        path('category=<category>', views.post_by_category, name='post_by_category' ),
    ]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
