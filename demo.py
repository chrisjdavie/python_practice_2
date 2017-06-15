""" A simple flask api that is visible through a docker containers.

The trick is "host='0.0.0.0'" in app.run - this exposes it to the local area
network (automatically done when launching a pre-built webserver typically,
which is why I didn't know this). 

"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

