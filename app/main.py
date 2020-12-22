from flask import Flask
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)


class SayHello(Resource):
    def get(self):
        return {'Hello': 'World'}


api.add_resource(SayHello, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
