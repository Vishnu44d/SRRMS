from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
api.add_resource(HelloWorld, '/')
class Myvalue(Resource):
    def get(self):
        return {'hello': 'Value', "he": 'not my fault'}
api.add_resource(Myvalue, '/val')

if __name__ == '__main__':
    app.run(debug=True)