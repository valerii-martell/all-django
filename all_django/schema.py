import graphene
import graphql_jwt

from graphql_api import schema, mutations


class Query(schema.Query,
            # schema.SomeAnotherQuery,
            graphene.ObjectType):
    pass


class Mutation(mutations.Mutation,
               # schema.SomeAnotherMutation,
               graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
