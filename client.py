from supabase import Client, create_client
import os

supabase_url = "https://vmlobhapeligtemjnuyo.supabase.co"
supabase_key = os.getenv("YOUR_SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(supabase_url, supabase_key)
# print(supabase_key)