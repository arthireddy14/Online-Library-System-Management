# update_stock.py
from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
# if not url or not key:
#     raise ValueError("Supabase credentials not found in environment variables")

 
def update_stock(product_id, new_stock):
    resp = sb.table("products").update({"stock": new_stock}).eq("product_id", product_id).execute()
    # if resp.error:
    #     print("Error:", resp.error)
    return resp.data
 
if __name__ == "__main__":
    pid = int(input("Enter product_id to update: ").strip())
    new_stock = int(input("Enter new stock value: ").strip())
 
    updated = update_stock(pid, new_stock)
    if updated:
        print("Updated record:", updated)
    else:
        print("No record updated — check product_id.")
# update_product.py
# import os
# from supabase import create_client, Client  # pip install supabase
# from dotenv import load_dotenv  # pip install python-dotenv

# load_dotenv()

# url = os.getenv("SUPABASE_URL")
# key = os.getenv("SUPABASE_KEY")
# sb: Client = create_client(url, key)


# def update_product(product_id: int, name=None, sku=None, price=None, stock=None):
#     """Update product details by product_id. Only provided fields will be updated."""
#     payload = {}

#     if name is not None:
#         payload["name"] = name
#     if sku is not None:
#         payload["sku"] = sku
#     if price is not None:
#         payload["price"] = price
#     if stock is not None:
#         payload["stock"] = stock

#     if not payload:
#         return {"error": "No fields to update"}

#     resp = (
#         sb.table("products")
#         .update(payload)
#         .eq("product_id", product_id)
#         .execute()
#     )
#     return resp.data


# if __name__ == "__main__":
#     prod_id = int(input("Enter product_id to update: ").strip())

#     print("Leave blank if you don't want to change a field.")
#     name = input("New name: ").strip() or None
#     sku = input("New SKU: ").strip() or None
#     price_in = input("New price: ").strip()
#     stock_in = input("New stock: ").strip()

#     price = float(price_in) if price_in else None
#     stock = int(stock_in) if stock_in else None

#     updated = update_product(prod_id, name, sku, price, stock)
#     print("Updated:", updated)

 