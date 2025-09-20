# 3. Update
# Update book stock (e.g., when more copies are purchased).
# Update member info (e.g., change email).

import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

# --- Update book stock ---
def update_book():
    try:
        bid = int(input("Enter book_id to update: ").strip())
        new_stock = int(input("Enter new stock value: ").strip())

        resp = sb.table("books").update({"stock": new_stock}).eq("book_id", bid).execute()

        if resp.data:
            print("Updated book stock:", resp.data)
        else:
            print("No book found with that ID.")
    except Exception as e:
        print("Error updating book:", e)

# --- Update member info (email, name, etc.) ---
def update_member():
    try:
        mid = int(input("Enter member_id to update: ").strip())
        new_email = input("Enter new email (leave blank to skip): ").strip()
        new_name = input("Enter new name (leave blank to skip): ").strip()

        payload = {}
        if new_email:
            payload["email"] = new_email
        if new_name:
            payload["name"] = new_name

        if not payload:
            print("No updates provided.")
            return

        resp = sb.table("members").update(payload).eq("member_id", mid).execute()

        if resp.data:
            print("Updated member info:", resp.data)
        else:
            print("No member found with that ID.")
    except Exception as e:
        print("Error updating member:", e)


if __name__=="__main__":
    print("1. Update book stock")
    print("2. Update member info")
    choice = int(input("Enter the choice: ").strip())

    if choice == 1:
        update_book()
    elif choice == 2:
        update_member()


# import os
# from supabase import create_client, Client
# from dotenv import load_dotenv

# load_dotenv()

# url = os.getenv("SUPABASE_URL")
# key = os.getenv("SUPABASE_KEY")
# sb: Client = create_client(url, key)

# def update_book():
    
# def update_member():
    
    
    
# if __name__=="__main__":
#     print("1.Update book stock")
#     print("2.Update member info")
#     choice=int(input("Enter the choice ").strip())
#     if(choice==1):
#         update_book()
#     elif(choice==2):
#         update_member()
    
    
    