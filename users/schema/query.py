import graphene
from graphene_django.filter import DjangoFilterConnectionField

from users.schema.node import UserFilter, UserNode


class Query(graphene.ObjectType):
    """
    Get 'me' data, that is current logged in user data
    """

    me = graphene.Field(UserNode)  # logged in user details

    def resolve_me(self, info):
        user = info.context.user
        return user
