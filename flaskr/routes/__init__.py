from flask_restx import Api

from flaskr.routes.simple.route import api as simple_api

api = Api(
    version='1.0',
    title='CI/CD TEST API',
    description='CI/CD TEST API',
    doc='/',
)

api.add_namespace(simple_api)
