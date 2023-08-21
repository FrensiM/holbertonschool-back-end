from flask import Flask
from flask_restful import Resource, Api

app = Flask("ImageApi")
api = Api(app)


image = {
    'image 1': {'title', 'Hello Class'},
    'image 2': {'title', 'Why like this'}
}


class Image(Resource):
    
    def get(self):
        return image


api.add_resource(Image, '/')

if __name__ == '__main__':
    app.run()
