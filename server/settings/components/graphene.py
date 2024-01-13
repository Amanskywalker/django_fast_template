# GraphQL lib configurations
GRAPHENE = {
    "SCHEMA": "server.schema.schema",
    "MIDDLEWARE": [
        'graphene_django.debug.DjangoDebugMiddleware',
    ],
}
