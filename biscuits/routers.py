class DjongoRouter:

    route_models = {"productdata"}

    def db_for_read(self, model, **hints):
        print(model._meta.object_name)
        if model._meta.object_name in self.route_models:
            return "djongo"
        return 'default'

    def db_for_write(self, model, **hints):

        if model._meta.object_name in self.route_models:
            return "djongo"
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        
        if (
            obj1._meta.object_name in self.route_models
            or obj2._meta.object_name in self.route_models
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print(model_name)
        if model_name in self.route_models:
            print('djongo')
            return db == "djongo"
        print('default')
        return None