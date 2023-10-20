# Seed data into the database
from faker import Faker
from random import choice as rc

from models import db, User, Post

from app import app

fake = Faker()


with app.app_context():
    User.query.delete()
    Post.query.delete()

    users = []

    for i in range(20):
        new_user = User(
            email=fake.email(),
            username=fake.first_name()
        )

        users.append(new_user)

    db.session.add_all(users)

    posts = []
    
    for i in range(50):
        new_post = Post(
            title=fake.text(15),
            body=fake.sentence(),
            user=rc(users)
        )

        posts.append(new_post)

    db.session.add_all(posts)
    db.session.commit()