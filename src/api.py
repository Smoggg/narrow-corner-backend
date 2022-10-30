from fastapi import FastAPI, Body

from src.blog_entry.model import BlogEntrySchema, UpdateBlogEntrySchema

app = FastAPI()

blog_entries = [
    {"id": 1, "title": "Donuts", "tags": ["Flour", "Milk", "Sugar", "Vegetable Oil"]}
]


@app.get("/", tags=["Home"])
def get_root() -> dict:
    return {"message": "Welcome to the app."}


@app.get("/blog_entry", tags=["BlogEntry"])
def get_blog_entries() -> dict:
    return {"data": blog_entries}


@app.get("/blog_entry/{id}", tags=["BlogEntry"])
def get_blog_entry(id: int) -> dict:
    if id > len(blog_entries) or id < 1:
        return {"error": "Invalid ID passed."}

    for blog_entry in blog_entries:
        if blog_entry["id"] == id:
            return {"data": [blog_entry]}

    return {"error": "No such blog_entry with ID {} exist".format(id)}


@app.post("/blog_entry", tags=["BlogEntry"])
def add_blog_entry(blog_entry: BlogEntrySchema = Body(...)) -> dict:
    blog_entry.id = len(blog_entries) + 1
    blog_entries.append(blog_entry.dict())
    return {"message": "Blog Entry added successfully."}


@app.put("/blog_entry", tags=["BlogEntry"])
def update_blog_entry(id: int, blog_entry_data: UpdateBlogEntrySchema) -> dict:

    # TODO
    return {"message": "Blog Entry updated successfully."}


@app.delete("/blog_entry/{id}", tags=["BlogEntry"])
def delete_blog_entry(id: int) -> dict:

    # TODO
    return {"message": "TBD Blog Entry deleted successfully."}
