from django.contrib import admin
from django.urls import path, include
from shortener.views import index, get_user, register,login_view, logout_view,list_view, url_list,url_create,url_change
import mimetypes
from shrinkers.settings import DEBUG
if DEBUG:
    import debug_toolbar

    mimetypes.add_type("application/javascript", ".js", True)

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("get_user/<int:user_id>", get_user),
    path("register", register, name="register"),
    path("list", list_view, name="list_view"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path('url_list', url_list, name="url_list"),
    path('urls/create',url_create, name="url_create"),
    path('urls/<str:action>/<int:url_id>/', url_change, name="url_change"),
]


# if DEBUG:
#     urlpatterns += [
#         path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
#     ]