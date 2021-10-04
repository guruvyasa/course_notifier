from flask import Flask, render_template, request, redirect
import database as db
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addEnquiry",methods=['GET', 'POST'])
def addEnquiry():
    if request.method == "GET":
        status = request.args.get("status",0)
        return render_template("enquiry.html", enquiries=db.getEnquiries(),status=status)
    else:
        student_name = request.form['student']
        phone = request.form['phone']
        course_name = request.form['course']
        status = db.addEnquiry(student_name, phone, course_name)
        return redirect("/addEnquiry?status="+status)

app.run(debug=True), 