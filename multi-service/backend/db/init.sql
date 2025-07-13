-- Create the blog_posts table
CREATE TABLE IF NOT EXISTS blog_posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some sample blog posts
INSERT INTO blog_posts (title, content) VALUES
  ('Welcome to the Blog', 'This is the first post seeded on container start.'),
  ('Another Seeded Post', 'This one was also inserted by init.sql.'),
  ('Docker + Postgres', 'Now you know how to seed Postgres automatically!');
