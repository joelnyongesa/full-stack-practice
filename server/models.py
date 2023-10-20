from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# defining our classes
class User(db.Model, SerializerMixin):

    __tablename__ = "users"

    serialize_rules = ("-posts.user",)

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    username = db.Column(db.String(10), unique=True, nullable=False)

    posts = db.relationship("Post", backref="user")

    def __repr__(self):
        return f"User: {self.id}\nEmail: {self.email}\nuUsername: {self.username}\n"


class Post(db.Model, SerializerMixin):

    __tablename__ = "posts"

    serialize_rules = ("-user.posts", )

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"Title: {self.title}\nBody: {self.body}"