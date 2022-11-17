from flask_restx import Api

from flaskr.routes.test.route import api as test_api

api = Api(
    version='1.0',
    title='CI/CD TEST API',
    description='CI/CD TEST API',
    doc='/',
)

api.add_namespace(test_api)
