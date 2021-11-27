from flask import Flask,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        json_recieved = request.get_json()
        return {'you have sent':json_recieved},201


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)