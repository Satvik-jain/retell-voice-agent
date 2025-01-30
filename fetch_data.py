from client import supabase

def fetch_data_from_supabase(query):
    try:
        response = supabase.table("Real Estate Listing")  
        result = response.select("*").ilike("Address", f"%{query}%").execute()

        if result['data']:
            return result['data']
        else:
            return [{"message": "No relevant data found."}]
    except Exception as error:
        return [{"message": f"Error fetching data: {error}"}]