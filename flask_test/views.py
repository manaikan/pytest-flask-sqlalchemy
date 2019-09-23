from werkzeug.exceptions import NotFound
from flask.views import MethodView
from flask import jsonify
from .models import Table

class TableView(MethodView) :

    __model__ = Table

    def resource(self, id):
        resource = self.__model__.query.get(id)
        if not resource:
            raise NotFound()
        return jsonify(resource)

    def resources(self):
        resources = self.__model__.query.all()
        return jsonify(resources)

    def get(self, key=None):
        if key :
            return self.resoource(key)
        else :
            return self.resources()


def register(router):
    router.add_url_rule("/table/", view_func = TableView.as_view("table"))