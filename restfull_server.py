from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
        
    def post(self):
        json_recieved = request.get_json()

        # return {'status':json_recieved},201
        
        if json_recieved.get('username','')=="tom" and json_recieved.get('password','')=='jerry':
            return {'status':True},201

        return {'status':False},400


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)