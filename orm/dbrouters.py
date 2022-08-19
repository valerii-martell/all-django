from .models import GameModel, GamerModel, GamerLibraryModel


class PostgreSQLDBRouter(object):
    """
    A router to control all database operations on models in some applications.
    """

    # router_models = [GameModel, GamerModel, GamerLibraryModel]
    route_app_labels = {"orm"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read models from postgresql.
        """
        if model._meta.app_label in self.route_app_labels:
            return "postgresql_db"
        # if model in self.router_models:
        #     return 'postgresql_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write models go to postgresql.
        """
        if model._meta.app_label in self.route_app_labels:
            return "postgresql_db"
        # if model in self.router_models:
        #     return 'postgresql_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the apps only appear in the
        'postgresql' database.
        """
        if app_label in self.route_app_labels:
            return db == "postgresql_db"
        return None
