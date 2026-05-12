from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Flask Application</h1>
    <p>Welcome to the Flask app!</p>
    """

@app.route("/api")
def api():
    data = {
        "message": "Hello from Flask API",
        "status": "success"
    }
    return jsonify(data)

@app.route("/about")
def about():
    return """
    <h2>About Page</h2>
    <p>This is a sample Flask application.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)