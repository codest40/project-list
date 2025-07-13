from flask import Blueprint, jsonify, current_app, request, render_template
from .models import db, BlogPost
import json

bp = Blueprint('blog', __name__)

@bp.route("/")
def view_posts():
   return render_template("/index.html")

@bp.route("/posts", methods=["GET"])
def get_posts():
    redis = current_app.redis_client

    # Check cache
    cached_posts = redis.get("all_posts")
    if cached_posts:
        return jsonify(json.loads(cached_posts)), 200

    # Not cached? Query DB
    posts = BlogPost.query.order_by(BlogPost.timestamp.desc()).all()
    data = [p.as_dict() for p in posts]

    # Store in Redis (60 sec TTL)
    redis.set("all_posts", json.dumps(data), ex=60)

    return jsonify(data), 200

@bp.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    new_post = BlogPost(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()

    # Invalidate cache
    redis = current_app.redis_client
    redis.delete("all_posts")

    return jsonify(new_post.as_dict()), 201
