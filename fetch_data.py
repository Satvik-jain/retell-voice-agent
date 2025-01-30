from client import supabase

def fetch_data_from_supabase(query, filters):
    try:
        # Initialize the query to search in the "Real Estate Listing" table
        response = supabase.table("Real Estate Listing")

        # Apply filters dynamically based on the request
        if 'bedrooms' in filters:
            response = response.filter('Bedrooms', 'eq', filters['bedrooms'])
        
        if 'bathrooms' in filters:
            response = response.filter('Bathrooms', 'eq', filters['bathrooms'])

        if 'kitchen' in filters:
            response = response.filter('Kitchen', 'eq', filters['kitchen'])

        if 'hall' in filters:
            response = response.filter('Hall', 'eq', filters['hall'])

        if 'parking_available' in filters:
            response = response.filter('Parking Available', 'eq', filters['parking_available'])

        if 'balcony' in filters:
            response = response.filter('Balcony', 'eq', filters['balcony'])

        if 'furnished' in filters:
            response = response.filter('Furnished', 'eq', filters['furnished'])

        if 'swimming_pool' in filters:
            response = response.filter('Swimming Pool', 'eq', filters['swimming_pool'])

        if 'number_of_parking_spaces' in filters:
            response = response.filter('Number of Parking Spaces', 'eq', filters['number_of_parking_spaces'])

        if 'garden' in filters:
            response = response.filter('Garden', 'eq', filters['garden'])

        if 'gym_facility' in filters:
            response = response.filter('Gym Facility', 'eq', filters['gym_facility'])

        if 'year_built' in filters:
            response = response.filter('Year Built', 'eq', filters['year_built'])

        if 'rent_min' in filters:
            response = response.filter('Rent per month (in USD)', 'gte', filters['rent_min'])
        
        if 'rent_max' in filters:
            response = response.filter('Rent per month (in USD)', 'lte', filters['rent_max'])
        
        if 'location' in filters:
            response = response.filter('Address', 'ilike', f"%{filters['location']}%")
        
        if 'moving_date' in filters:
            response = response.filter('Moving Date', 'eq', filters['moving_date'])

        # Execute the query and return the result
        result = response.execute()

        if result['data']:
            return result['data']
        else:
            return [{"message": "No relevant data found."}]
    
    except Exception as error:
        return [{"message": f"Error fetching data: {error}"}]