from client import supabase

from client import supabase
from flask import Flask, request, jsonify

app = Flask(__name__)

from client import supabase
from flask import Flask, request, jsonify

app = Flask(__name__)

def fetch_data_from_supabase(query, filters):
    try:
        response = supabase.table("Real Estate Listing")

        if 'bedrooms' in filters:
            response = response.eq("Bedrooms", filters['bedrooms'])

        if 'bathrooms' in filters:
            response = response.eq("Bathrooms", filters['bathrooms'])

        if 'kitchen' in filters:
            response = response.eq("Kitchen", filters['kitchen'])

        if 'hall' in filters:
            response = response.eq("Hall", filters['hall'])

        if 'parking_available' in filters:
            response = response.eq("Parking Available", filters['parking_available'])

        if 'balcony' in filters:
            response = response.eq("Balcony", filters['balcony'])

        if 'furnished' in filters:
            response = response.eq("Furnished", filters['furnished'])

        if 'swimming_pool' in filters:
            response = response.eq("Swimming Pool", filters['swimming_pool'])

        if 'number_of_parking_spaces' in filters:
            response = response.eq("Number of Parking Spaces", filters['number_of_parking_spaces'])

        if 'garden' in filters:
            response = response.eq("Garden", filters['garden'])

        if 'gym_facility' in filters:
            response = response.eq("Gym Facility", filters['gym_facility'])

        if 'year_built' in filters:
            response = response.eq("Year Built", filters['year_built'])

        if 'rent_min' in filters:
            response = response.gte("Rent per month (in USD)", filters['rent_min'])
        
        if 'rent_max' in filters:
            response = response.lte("Rent per month (in USD)", filters['rent_max'])
        
        if 'location' in filters:
            response = response.ilike("Address", f"%{filters['location']}%")
        
        if 'moving_date' in filters:
            response = response.eq("Moving Date", filters['moving_date'])

        result = response.execute()

        print(f"Filters applied: {filters}")

        if result.data:
            return result.data
        else:
            return [{"message": "No relevant data found."}]
    
    except Exception as error:
        return [{"message": f"Error fetching data: {error}"}]