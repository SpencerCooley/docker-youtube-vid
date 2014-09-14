from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # ... the rest of your URLconf goes here ...
# Examples:
url(r'^$', 'views.home', name='home'),

url(r'another/', 'views.another', name='another'),
# url(r'^blog/', include('blog.urls')),

url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
