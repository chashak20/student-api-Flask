from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample Data
students = {
    "Rohan": 55,
    "Tasnim": 50,
    "Reshmita": 60,
    "Vipul": 77,
    "Raj": 60
}

# ---------------- HOME ----------------
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Flask Student API",
        "routes": {
            "GET all students": "/students",
            "GET single student": "/students/<name>",
            "POST add student": "/add"
        }
    })

# ---------------- GET ALL ----------------
@app.route("/students")
def get_students():
    return jsonify(students)

# ---------------- GET ONE ----------------
@app.route("/students/<name>")
def get_student(name):
    if name in students:
        return jsonify({name: students[name]})
    return jsonify({"error": "Student not found"}), 404

# ---------------- ADD ----------------
@app.route("/add", methods=["POST"])
def add_student():
    data = request.get_json()

    name = data.get("name")
    marks = data.get("marks")

    if not name or not marks:
        return jsonify({"error": "Invalid data"}), 400

    students[name] = marks
    return jsonify({"message": "Student added successfully"})

# ---------------- DELETE ----------------
@app.route("/delete/<name>", methods=["DELETE"])
def delete_student(name):
    if name in students:
        del students[name]
        return jsonify({"message": "Student deleted"})
    return jsonify({"error": "Student not found"}), 404


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)