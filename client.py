from supabase import Client, create_client

supabase_url = "https://vmlobhapeligtemjnuyo.supabase.co"
supabase_key = "YOUR_SUPABASE_SERVICE_ROLE_KEY"

supabase = create_client(supabase_url, supabase_key)