from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Complaint Class
class Complaint:
    complaint_id = 1

    def __init__(self, student_name, room_no, issue):
        self.id = Complaint.complaint_id
        Complaint.complaint_id += 1

        self.student_name = student_name
        self.room_no = room_no
        self.issue = issue
        self.status = "Pending"

# Complaint Storage
complaints = []

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Register Complaint
@app.route('/register', methods=['POST'])
def register():
    data = request.json

    complaint = Complaint(
        data['student_name'],
        data['room_no'],
        data['issue']
    )

    complaints.append(complaint)

    return jsonify({
        "message": "Complaint Registered Successfully",
        "complaint_id": complaint.id
    })

# View Complaints
@app.route('/complaints', methods=['GET'])
def view_complaints():
    complaint_list = []

    for c in complaints:
        complaint_list.append({
            "id": c.id,
            "student_name": c.student_name,
            "room_no": c.room_no,
            "issue": c.issue,
            "status": c.status
        })

    return jsonify(complaint_list)

# Search Complaint
@app.route('/search/<int:complaint_id>', methods=['GET'])
def search_complaint(complaint_id):
    for c in complaints:
        if c.id == complaint_id:
            return jsonify({
                "id": c.id,
                "student_name": c.student_name,
                "room_no": c.room_no,
                "issue": c.issue,
                "status": c.status
            })

    return jsonify({"message": "Complaint Not Found"}), 404

# Resolve Complaint
@app.route('/resolve/<int:complaint_id>', methods=['PUT'])
def resolve_complaint(complaint_id):
    for c in complaints:
        if c.id == complaint_id:
            c.status = "Resolved"

            return jsonify({
                "message": "Complaint Resolved Successfully"
            })

    return jsonify({"message": "Complaint Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
