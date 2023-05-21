import json
import logging
from datetime import datetime, timedelta
from random import randint

from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.gis.db import models
from django.contrib.gis.geos import fromstr, Point
from django.db.models import Q

import django_filters
import graphene
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id

# Permissions
from users.permission.permission import UserPermission
from users.permission.graphql.permission import AllowAuthenticated, AllowStaff, AllowAny

# get Nodes definitions
from users.schema.node import UserNode

# Get an instance of a logger
logger = logging.getLogger(__name__)


class UpdateUser(graphene.relay.ClientIDMutation):
    user = graphene.Field(UserNode)

    class Input:
        name = graphene.String(required=False)
        email = graphene.String(required=False)

    def mutate_and_get_payload(root, info, **input):
        if not UserPermission.hasPermission(UserPermission, info, [AllowAuthenticated]):
            raise Exception("Unauthorized")

        user = info.context.user

        try:
            # update the details if they have been entered
            if input.get("name") is not None:
                user.name = input.get("name")
            if input.get("email") is not None:
                user.email = input.get("email")

            user.save()
        except Exception as e:
            raise Exception(f"Error Saving user details : {str(e)}")

        return UpdateUser(user=user)


class Mutation(graphene.ObjectType):
    update_user_details = UpdateUser.Field()
