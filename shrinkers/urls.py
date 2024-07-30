from django.contrib import admin
from django.urls import path, include
from shortener.views import index, get_user, register,login_view, logout_view
import debug_toolbar
import mimetypes
mimetypes.add_type("application/javascript", ".js", True)

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("get_user/<int:user_id>", get_user),
    path("register", register, name="register"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
]


