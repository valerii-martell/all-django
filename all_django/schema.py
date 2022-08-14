import graphene
from graphql_api import schema


class Query(schema.Query,
            # schema.SomeAnotherQuery,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
