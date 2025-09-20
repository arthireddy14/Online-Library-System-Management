# 2. Read (Select)
# List all books with availability.
# Search books by title/author/category.
# Show member details and their borrowed books.
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def display_books():
    resp=sb.table("books").select("*").order("book_id",desc=False).execute()
    return resp.data
    

def search_book(keyword:str):
    resp=(
        sb.table("books").select("*").or_(f"title.ilike.%{keyword}%,author.ilike.%{keyword}%,category.ilike.%{keyword}%").execute()
    )
    return resp.data
def member_borrowed_books():
    # Supabase doesn't support multi-table joins directly → need RPC or multiple queries
    members = sb.table("members").select("*").execute().data
    borrows = sb.table("borrow_records").select("member_id, book_id, borrow_date, return_date").execute().data
    books = sb.table("books").select("book_id, title").execute().data
    book_map = {b["book_id"]: b["title"] for b in books}

    for m in members:
        print(f"\nMember: {m['name']} ({m['email']})")
        borrowed = [br for br in borrows if br["member_id"] == m["member_id"]]
        if borrowed:
            for br in borrowed:
                print(f"  - {book_map.get(br['book_id'], 'Unknown')} (Borrowed: {br['borrow_date']}, Returned: {br['return_date']})")
        else:
            print("  - No borrowed books")

if __name__=="__main__":
    
    print("1.List all books")
    print("2.Search book")
    print("3.Show member details,borrowed books")
    choice=int(input("Enter your choice ").strip())
    
    if(choice==1):
        books=display_books()
        if books:
            print("Book details ")
            for b in books:
                availability="Available" if(b['stock']>0) else "Out of stock"
                print(f"{b['book_id']},{b['title']}->{b['author']},{b['category']},{b['stock']}->{availability}")
        else:
            print("No books found")
    elif(choice==2):
        print("Search book by title,author,category")
        x=input("Enter book detail ")
        book=search_book(x)
        if book:
            print("Book details ")
            for b in book:
                availability="Available" if(b['stock']>0) else "Out of stock"
                print(f"{b['book_id']},{b['title']}->{b['author']},{b['category']},{b['stock']}->{availability}")
        else:
            print("No books found")
    elif(choice==3):
        print("member details and their borrowed books")
        member_borrowed_books()
        

    
        

    