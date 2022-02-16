from django.contrib import admin

from django.urls import include, path
from rest_framework import routers
from api import views

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
#router.register(r"users", views.UserViewSet)
#router.register(r"groups", views.GroupViewSet)

### Views set at ./api
router.register(r"posts", views.PostsViewSet)
router.register(r"text", views.TextViewSet)
router.register(r"artifact", views.ArtifactViewSet)
router.register(r"activity", views.ActivityViewSet)
router.register(r"assets", views.AssetsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, login URLs included for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # OpenAPI 3 documentation with Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]
