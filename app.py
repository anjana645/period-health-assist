from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reverse", methods=["POST"])
def reverse_string():
    data = request.json  # Get JSON data from frontend
    user_text = data.get("message", "")

    reversed_text = user_text[::-1]  # Reverse the string

    return jsonify({"response": reversed_text})  # Send JSON response

if __name__ == "__main__":
    app.run(debug=True)

