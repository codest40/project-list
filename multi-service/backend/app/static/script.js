const apiBase = 'http://localhost:5000'; // Update if behind proxy

async function loadPosts() {
  const res = await fetch(`${apiBase}/posts`);
  const posts = await res.json();
  const postsDiv = document.getElementById("posts");
  postsDiv.innerHTML = '';

  if (posts.length === 0) {
    postsDiv.innerHTML = "<p>No posts yet.</p>";
    return;
  }

  posts.forEach(post => {
    const div = document.createElement("div");
    div.className = "post";
    div.innerHTML = `<h3>${post.title}</h3><p>${post.content}</p><small>${new Date(post.timestamp).toLocaleString()}</small>`;
    postsDiv.appendChild(div);
  });
}

document.getElementById("postForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = document.getElementById("title").value.trim();
  const content = document.getElementById("content").value.trim();

  const res = await fetch(`${apiBase}/posts`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, content })
  });

  if (res.ok) {
    document.getElementById("postForm").reset();
    await loadPosts();
  }
});

loadPosts();
