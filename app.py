from flask import Flask, request, jsonify
from fetch_data import fetch_data_from_supabase

app = Flask(__name__)

@app.route("/retell", methods=["POST"])
@app.route("/retell", methods=["POST"])
def retell_custom_function():
    data = request.get_json()
    
    # Check if query is part of the incoming JSON
    if not data or "query" not in data:
        return jsonify({"error": "Query is required"}), 400

    response = fetch_data_from_supabase(data["query"])
    return jsonify({"result": response})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
