from flask_restx import Namespace, Resource

api = Namespace('simple')


@api.route('')
class Route(Resource):
    def get(self):
        return 'Response of GET Request'

    def post(self):
        return 'Response of POST Request'
