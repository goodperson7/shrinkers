from django.contrib import admin
from django.urls import path, include
from shortener.urls.views import url_redirect
import mimetypes
from shrinkers.settings import DEBUG
if DEBUG:
    import debug_toolbar

    mimetypes.add_type("application/javascript", ".js", True)

urlpatterns = [

    path('admin/', admin.site.urls),
    path("", include("shortener.index.urls")),
    path("urls/", include("shortener.urls.urls")),
    path("<str:prefix>/<str:url>",url_redirect),
    # path('urls/create',url_create, name="url_create"),
    # path('urls/<str:action>/<int:url_id>/', url_change, name="url_change"),
]


if DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
    ]