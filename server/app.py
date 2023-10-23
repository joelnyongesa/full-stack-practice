from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_cors import CORS

from models import db, User, Post

app = Flask(__name__)

api=Api(app)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# End points for our API
class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]

        response = make_response(
            jsonify(users),
            200
        )

        return response
    
    def post(self):
        new_user = User(
            email=request.get_json()["email"],
            username=request.get_json()["username"]
        )

        db.session.add(new_user)
        db.session.commit()

        new_user_dict = new_user.to_dict()

        response = make_response(
            jsonify(new_user_dict),
            201
        )

        return response    

api.add_resource(Users, "/users")

class UserByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first().to_dict()

        response = make_response(
            jsonify(user),
            200
        )

        return response
    
    def patch(self, id):
        user = User.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(user, attr, request.get_json()[attr])

        db.session.add(user)
        db.session.commit()

        user_dict = user.to_dict()

        response = make_response(
            jsonify(user_dict),
            200
        )

        response.headers["Content-Type"] = "application/json"

        return response
    
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        response = jsonify({"message": "user deleted successfully!"}, 200)

        return response
    
api.add_resource(UserByID, '/users/<int:id>')

class Posts(Resource):
    def get(self):
        posts = [post.to_dict() for post in Post.query.all()]

        response = make_response(
            jsonify(posts),
            200
        )

        return response
    
    def post(self):
        new_post = Post(
            title=request.get_json()["title"],
            body=request.get_json()["body"],
            user_id=request.get_json()["user_id"]
        )

        db.session.add(new_post)
        db.session.commit()

        new_post_dict = new_post.to_dict()

        response = make_response(
            jsonify(new_post_dict),
            201
        )

        return response
    

api.add_resource(Posts, '/posts')

class PostsByID(Resource):
    def get(self, id):
        post = Post.query.filter_by(id=id).first().to_dict()

        response = make_response(
            jsonify(post),
            200
        )

        return response
    
    def patch(self, id):
        post = Post.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(post, attr, request.get_json()[attr])

        db.session.add(post)
        db.session.commit()
        

        post_dictionary = post.to_dict()

        response = make_response(
            jsonify(post_dictionary),
            200
        )

        return response
    
    def delete(self, id):
        post = Post.query.filter_by(id=id).first()

        db.session.delete(post)
        db.session.commit()

        response = make_response(
            jsonify({"message": "post deleted successfully!"}),
            200
        )

        return response
    
api.add_resource(PostsByID, '/posts/<int:id>')