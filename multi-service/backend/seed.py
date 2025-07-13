# seed.py
from app import create_app, db
from app.models import BlogPost
from datetime import datetime, timedelta
import random

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    base_time = datetime.utcnow()
    posts = []

    for i in range(1, 21):
        post = BlogPost(
            title=f"Seed Post {i}",
            content=f"This is the content of seed post number {i}.",
            timestamp=base_time - timedelta(days=random.randint(0, 100))
        )
        posts.append(post)

    db.session.add_all(posts)
    db.session.commit()
    print("✅ Database seeded with 20 blog posts.")
