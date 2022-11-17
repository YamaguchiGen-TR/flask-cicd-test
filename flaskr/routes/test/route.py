from flask_restx import Namespace, Resource

api = Namespace('upload')


@api.route('')
class Route(Resource):
    def get(self):
        return 'GET Request'

    def post(self):
        return 'POST Request'
