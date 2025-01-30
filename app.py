from flask import Flask, request, jsonify
from fetch_data import fetch_data_from_supabase

app = Flask(__name__)

@app.route("/retell", methods=["POST"])
def retell_custom_function():
    data = request.get_json()
    query = data.get("query")
    
    if not query:
        return jsonify({"error": "Query is required"}), 400

    # Fetch data from Supabase
    response = fetch_data_from_supabase(query)
    
    return jsonify({"result": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
