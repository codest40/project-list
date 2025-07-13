from flask import Flask
from .models import db
import redis
import os

def create_app():
    app = Flask(__name__)

    # DB Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "postgresql://admin:securepassword@db:5432/blog_db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Redis setup
    app.redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

    from .routes import bp as blog_bp
    app.register_blueprint(blog_bp)

    return app
