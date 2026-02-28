from fastapi import FastAPI, HTTPException

app = FastAPI()


text_posts = {
    1: {"title": "Getting Started with FastAPI", "content": "FastAPI is a modern web framework for building APIs with Python."},
    2: {"title": "Understanding REST APIs", "content": "REST stands for Representational State Transfer and is an architectural style."},
    3: {"title": "Python Tips and Tricks", "content": "Here are some useful Python tips to improve your code quality."},
    4: {"title": "Introduction to Docker", "content": "Docker allows you to package applications into containers for easy deployment."},
    5: {"title": "Working with Databases", "content": "Learn how to connect FastAPI with PostgreSQL using SQLAlchemy."},
    6: {"title": "Authentication in APIs", "content": "Implementing JWT authentication to secure your API endpoints."},
    7: {"title": "Async Programming in Python", "content": "Using async and await to write non-blocking Python code."},
    8: {"title": "API Testing Best Practices", "content": "How to write proper tests for your API using pytest and httpx."},
    9: {"title": "Deploying with Docker Compose", "content": "Using Docker Compose to manage multi-container applications."},
    10: {"title": "Environment Variables and Config", "content": "Managing configuration and secrets using environment variables in FastAPI."},
}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}


@app.get("/posts")
def get_all_posts():
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="post not found")

    return text_posts.get(id)
