class MySQLDBRouter(object):
    """
    A router to control all database operations on models in some applications.
    """
    # router_models = [GameModel, GamerModel, GamerLibraryModel]
    route_app_labels = {'graphql_api'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read models from mysql.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'mysql_db'
        # if model in self.router_models:
        #     return 'mysql_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write models go to mysql.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'mysql_db'
        # if model in self.router_models:
        #     return 'mysql_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the apps is
        involved.
        """
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the apps only appear in the
        'mysql' database.
        """
        if app_label in self.route_app_labels:
            return db == 'mysql_db'
        return None
