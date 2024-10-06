from flask import Flask,render_template,request,redirect,url_for
from flask import session

import sqlite3 as sql

app=Flask(__name__)
app.secret_key="mohanraj"


@app.route("/")
def index():
	return render_template("2a.html")

@app.route("/home",methods=["POST"])
def login():
	name=request.form.get("name")
	password=request.form.get("password")
	conn=sql.connect("main.db")
	cursor=conn.cursor()
	cursor.execute("select * from student where email=? AND DOB=?",(name,password));
	data=cursor.fetchone();
	conn.close()
	if data:
		session['username']=name;
		session['password']=password;
		return redirect(url_for('dashboard'))

    

	else:
		return render_template("11.html")

@app.route('/dashboard')
def dashboard():
    return render_template('2.html')


@app.route('/user_details')
def user_details():
	conn=sql.connect("main.db")
	cursor=conn.cursor()
	username=session['username']
	password=session['password']
	cursor.execute("select * from student where email=? and DOB=?",(username,password))
	userdetails=cursor.fetchone()
	conn.close();
	return render_template('user_details_embedded.html',user_details=userdetails)

@app.route("/signout")
def signout():
	return render_template("1.html")


@app.route("/about")
def about():
	return render_template("about.html")


@app.route("/register")
def register():
	return render_template("r1.html")


@app.route("/student")
def student():
	return render_template("2a.html")

@app.route("/faculty")
def faculty():
	return  render_template("faculty.html")



@app.route("/reg",methods=["POST"])
def reg():
	name=request.form.get("name")
	father=request.form.get("Father")
	gender=request.form.get("Gender")
	dob=request.form.get("dateof")
	email=request.form.get("email")
	mark=request.form.get("marks")
	rank=request.form.get("rank")
	telephone=request.form.get("telephone")
	Address=request.form.get("address")
	coursetype=request.form.get("type")
	coursename=request.form.get("course")


	with sql.connect("main.db") as con:
		cur=con.cursor()
		if name!="" and father!="" and  email!="" and rank!="" and telephone!="":
			cur.execute("SELECT * FROM STUDENT WHERE telephone=?",(telephone,))
			existing=cur.fetchall()


			if existing==[]:
				cur.execute("INSERT INTO STUDENT VALUES(?,?,?,?,?,?,?,?,?,?,?)",(name,father,gender,dob,email,mark,rank,telephone,Address,coursetype,coursename))
			else:
				return render_template("existing.html")

		else:
			return redirect(("register"))
		con.commit()
		return render_template("success.html")
		con.close()


@app.route('/list2')
def list2():
	con=sql.connect("main.db")
	con.row_factory=sql.Row

	cur=con.cursor()
	cur.execute("SELECT * FROM STUDENT")

	rows=cur.fetchall()
	return render_template("list2.html",rows=rows)


@app.route("/back")
def back():
	return render_template("2a.html")


@app.route("/already")
def already():
	return render_template("alread.html")


@app.route("/admin")
def admin():
 	return redirect(request.referrer)

@app.route("/cutoff")
def cutoff():
	return render_template("cutoff.html")
departments={
	"Information Technology":{"username":"faculty","password":"2024IT"},
	"Computer Science Engineering":{"username":"faculty","password":"2024CSE"},
	"Electrical and Communication Engineering":{"username":"faculty","password":"2024ECE"},
	"Electrical Engineering":{"username":"faculty","password":"2024EEE"},
	"Mechanical Engineering":{"username":"faculty","password":"2024MECH"},
	"Civil Engineering":{"username":"faculty","password":"2024CIVIL"},
	"Master of Business Administration":{"username":"faculty","password":"2024MBA"},
	"M.E Energy Engineering":{"username":"faculty","password":"2024MEEE"},
	"M.E Civil Engineering":{"username":"faculty","password":"2024MECIVIL"},
	"M.E Computer Science Engineering":{"username":"faculty","password":"2024MECSE"}
}

@app.route("/login1",methods=["POST"])
def login1():
	username=request.form.get("name")
	password=request.form.get("password")
	for department,cred in departments.items():
		if username==cred['username'] and password==cred['password']:
			session['dep']=department;
			return redirect(url_for("listing"))
		elif username=="admin" and password=="admin":
			return render_template("admin.html")
	return render_template("not.html")		
				

@app.route('/listing')
def listing():
	dep=session['dep']
	return render_template("department.html",dep=dep)

@app.route('/students')
def students():
				department=session['dep']
				con=sql.connect("main.db")
				con.row_factory=sql.Row
                
				cur=con.cursor()
				cur.execute('SELECT * FROM STUDENT WHERE COURSENAME=?',(department,))
				rows=cur.fetchall()
				print(rows)
				return render_template("list2.html",rows=rows)
				
				


if __name__=="__main__":
	app.run(debug=True)
