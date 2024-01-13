from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import (
    authentication_classes,
    api_view,
)
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import request as rq
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework.settings import api_settings
from .schema import schema

class DRFAuthenticateGraphQLView(GraphQLView):
    """
    This is overriding the GraphQL default view authentication with DRF authentication, 
    this makes the DRF use for the authentication work.
    """

    def parse_body(self, request):
        if isinstance(request, rq.Request):
            return request.data
        return super(DRFAuthenticateGraphQLView, self).parse_body(request)

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = authentication_classes(api_settings.DEFAULT_AUTHENTICATION_CLASSES)(view)
        view = api_view(["GET", "POST"])(view)
        return view


urlpatterns = [ 
    path(
            "graph",
            csrf_exempt(
                DRFAuthenticateGraphQLView.as_view(graphiql=True, schema=schema)
            ),
        )
    ]

# Change graphiql=True to graphiql=False if you do not want to use the GraphiQL API browser
if settings.DEV:
    urlpatterns = [
        path('admin/', admin.site.urls),
        # Swagger UI
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI:
        path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ] + urlpatterns
