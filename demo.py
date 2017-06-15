""" A simple flask api that is visible through a docker containers.

The trick is "host='0.0.0.0'" in app.run - this exposes it to the local area
network (automatically done when launching a pre-built webserver typically,
which is why I didn't know this). 

Docker needs to be run with "--expose 5000" (or whatever port is being used).
The lan ip of the docker container can be found with "ip addr show" (this is
usually aliased to "ifconfig", but normally my docker containers are 
lightweight enough to not have that.
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
    
