from supabase import create_client
import os

def test_supabase_permissions():
    supabase_url = "https://vmlobhapeligtemjnuyo.supabase.co"
    supabase_key = os.getenv("YOUR_SUPABASE_SERVICE_ROLE_KEY")
    
    if not supabase_key:
        return "ERROR: No Supabase key found in environment variables"
    
    supabase = create_client(supabase_url, supabase_key)
    
    try:
        # Test 1: Basic Read
        print("Testing basic read...")
        read_result = supabase.table("Real Estate Listing").select("*").limit(1).execute()
        print(f"Read Test: {'Success' if read_result.data else 'Failed'}")
        
        # Test 2: Table Existence
        print("\nTesting table access...")
        tables_result = supabase.table("Real Estate Listing").select("*").limit(1).execute()
        print(f"Table Access: {'Success' if tables_result.data is not None else 'Failed'}")
        
        # Test 3: RLS Policies (if any)
        print("\nTesting detailed read with filters...")
        filtered_result = supabase.table("Real Estate Listing").select("*").eq("bedrooms", 3).limit(1).execute()
        print(f"Filtered Read: {'Success' if filtered_result.data is not None else 'Failed'}")
        
        return "All tests completed. Check the results above."
        
    except Exception as e:
        return f"Error during testing: {str(e)}"

if __name__ == "__main__":
    print("Starting Supabase permission tests...")
    result = test_supabase_permissions()
    print("\nFinal Result:", result)