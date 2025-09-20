# 1. Create (Insert)
# Register new members (add_member(name, email)).
# Add new books (add_book(title, author, category, stock)).

# library_ops.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

# 1. Register new member
def add_member(name: str, email: str):
    payload = {"name": name, "email": email}
    resp = sb.table("members").insert(payload).execute()
    return resp.data

# 2. Add new book
def add_book(title: str, author: str, category: str, stock: int):
    payload = {"title": title, "author": author, "category": category, "stock": stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data

if __name__ == "__main__":
    print("1. Add Member")
    print("2. Add Book")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Enter member name: ").strip()
        email = input("Enter member email: ").strip()
        created = add_member(name, email)
        print("Member added:", created)

    elif choice == "2":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        category = input("Enter category: ").strip()
        stock = int(input("Enter stock: ").strip())
        created = add_book(title, author, category, stock)
        print("Book added:", created)

    