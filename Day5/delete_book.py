import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

# --- Delete a member (only if no borrowed books) ---
def delete_member():
    try:
        mid = int(input("Enter member_id to delete: ").strip())

        # check if member has any borrowed books
        borrowed = sb.table("borrow_records").select("*").eq("member_id", mid).execute().data
        if borrowed:
            print("Cannot delete — member has borrowed books.")
            return

        resp = sb.table("members").delete().eq("member_id", mid).execute()

        if resp.data:
            print("Member deleted:", resp.data)
        else:
            print("No member found with that ID.")
    except Exception as e:
        print("Error deleting member:", e)


# --- Delete a book (only if not borrowed) ---
def delete_book():
    try:
        bid = int(input("Enter book_id to delete: ").strip())

        # check if book is borrowed
        borrowed = sb.table("borrow_records").select("*").eq("book_id", bid).execute().data
        if borrowed:
            print("Cannot delete — book is borrowed by a member.")
            return

        resp = sb.table("books").delete().eq("book_id", bid).execute()

        if resp.data:
            print("Book deleted:", resp.data)
        else:
            print("No book found with that ID.")
    except Exception as e:
        print("Error deleting book:", e)


if __name__ == "__main__":
    print("1. Delete member")
    print("2. Delete book")
    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        delete_member()
    elif choice == 2:
        delete_book()
