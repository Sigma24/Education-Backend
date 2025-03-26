import pyodbc
from flask import request, jsonify, Blueprint
import  datetime
import random
def get_connection():

    try:
        conn = pyodbc.connect(

            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=LIVW1012\\SQLEXPRESS;"
            "DATABASE=system;"
            "Trusted_Connection=yes;"
)

        return conn

    except Exception as e:
        print (f"Database Connection Failed {e}")



Authentication = Blueprint('User', __name__)
@Authentication.route('/Admin', methods= ['POST'])
def Registration():
    try:
        data = request.get_json()

        name=data["name"]
        email = data["email"]
        password = data["password"]



        current_date = datetime.date.today()


        con  =get_connection()
        cursor = con.cursor()
        cursor.execute(
             "insert into Admin( Name, Email , Password,Date_Joined) Values (?,?,?,?)",
            (name,email,password,current_date)
        )
        con.commit()
        cursor.close()
        con.close()

        return jsonify({"message" : "use inserted successfully"})

    except Exception as e :
        return jsonify({"message":f"error inserting user {e}"})

@Authentication.route('/RegisterStudent', methods= ['POST'])
def RegistrationStudent():
    try:
        data = request.get_json()

        name=data["name"]
        email = data["email"]
        password = data["password"]
        age = data["age"]
        unique_code = str(random.randint(1000,9999))




        current_date = datetime.date.today()


        con  =get_connection()
        cursor = con.cursor()
        cursor.execute(
             "insert into Students( Name, Email , Password,Age,Unique_code,Date_Joined) Values (?,?,?,?,?,?)",
            (name,email,password,age,unique_code,current_date)
        )
        con.commit()
        cursor.close()
        con.close()

        return jsonify({"message" : "use inserted successfully"})

    except Exception as e :
        return jsonify({"message":f"error inserting user {e}"})

@Authentication.route('/RegisterTeacher', methods= ['POST'])
def RegistrationTeacher():
    try:
        data = request.get_json()

        name=data["name"]
        email = data["email"]
        password = data["password"]
        age = data["age"]
        unique_code = str(random.randint(1000,9999))
        current_date = datetime.date.today()


        con  =get_connection()
        cursor = con.cursor()
        cursor.execute(
             "insert into Teachers( Name, Email , Password,Age,Unique_code,Date_Joined) Values (?,?,?,?,?,?)",
            (name,email,password,age,unique_code,current_date)
        )
        con.commit()
        cursor.close()
        con.close()

        return jsonify({"message" : "user inserted successfully"})

    except Exception as e :
        return jsonify({"message":f"error inserting user {e}"})




@Authentication.route('/RegisterTutor', methods= ['POST'])
def RegistrationTutor():
    try:
        data = request.get_json()

        name=data["name"]
        email = data["email"]
        password = data["password"]
        age = data["age"]
        unique_code = str(random.randint(1000,9999))
        current_date = datetime.date.today()


        con  =get_connection()
        cursor = con.cursor()
        cursor.execute(
             "insert into Tutors( Name, Email , Password,Age,Unique_code,Date_Joined) Values (?,?,?,?,?,?)",
            (name,email,password,age,unique_code,current_date)
        )
        con.commit()
        cursor.close()
        con.close()

        return jsonify({"message" : "user inserted successfully"})

    except Exception as e :
        return jsonify({"message":f"error inserting user {e}"})




@Authentication.route("/login" , methods=["POST"])
def Login():
    try:
        data = request.get_json()
        identifier = data["identifier"]
        password = data["password"]

        admin = query_user("Admin" , "Email",identifier,password)

        if admin:
            return jsonify({
                "id":admin[0],
                "role":"Admin",
                "name":admin[1],
                 "email":admin[2]
            })

        student = query_user("Students","Unique_code",identifier,password)
        if student:
           return   jsonify({
               "id":student[0],
               "role":"Student",
               "name": student[1],
               "unique_code":student[5],
               "email":student[2],
               "age":student[4],
               "date":student[6]

           })

        Teacher= query_user("Teachers", "Unique_code", identifier, password)
        if Teacher:
            return jsonify({
                "id":Teacher[0],
                "role": "Teacher",
                "name": Teacher[1],
                "unique_code": Teacher[5],
                "email": Teacher[2],
                "age": Teacher[4],
                "date": Teacher[6]


            })
        Tutor = query_user("Tutors", "Unique_code", identifier, password)
        if Tutor:
            return jsonify({
                "id":Tutor[0],
                "role": "Tutor",
                "name": Tutor[1],
                "unique_code": Tutor[5]

            })




    except Exception as e:
        return jsonify({"message":f"error {e}"})


def query_user(table,identifier_field,identifier,password):
    try:
        con = get_connection()
        cursor = con.cursor()
        query = f"Select * from {table} where {identifier_field}=? and {password}=?"
        cursor.execute(query,(identifier,password))
        user=cursor.fetchone()
        cursor.close()
        con.close()
        return user
    except Exception  as e:
        return jsonify({"message":f"error{e}"})



@Authentication.route("/getStudents",methods=["GET"])
def getstudents():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("select * from Students")
        students = cursor.fetchall()
        data = [{"id": student[0], "name": student[1]} for student in students]
        cursor.close()
        con.close()
        return jsonify(data)
    except Exception as e :
        return jsonify({"message": f"error{e}"})


@Authentication.route("/getSubjects",methods=["GET"])
def getSubjects():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("select * from Subjects")
        students = cursor.fetchall()
        data = [{"id": student[0], "name": student[1]} for student in students]
        cursor.close()
        con.close()
        return jsonify(data)
    except Exception as e :
        return jsonify({"message": f"error{e}"})



@Authentication.route('/Grades', methods=['POST'])
def Grades():
        try:
            data = request.get_json()

            sID = data["sID"]
            tID = data["tID"]
            suID = data["suID"]
            grades = data["grades"]
            sID = int(sID)
            tID = int(tID)

            current_date = datetime.date.today()

            con = get_connection()
            cursor = con.cursor()
            cursor.execute(
                "insert into Predicted_Grades(Teacher_ID , Student_ID,Subject_ID,Date,Grade) Values (?,?,?,?,?)",
                (tID, sID, suID, current_date, grades)
            )
            con.commit()
            cursor.close()
            con.close()

            return jsonify({"message": "user inserted successfully"})

        except Exception as e:
            return jsonify({"message": f"error{e}"})




@Authentication.route('/StudentGrades', methods=['GET'])
def StudentGrades():
    try:
        student_id = request.args.get('sID')

        con = get_connection()
        cursor = con.cursor()


        query = """
            SELECT 
                t.Name AS Teacher_Name, 
                s.Subject_Name, 
                pg.Grade
            FROM 
                Predicted_Grades pg
            INNER JOIN Teachers t ON pg.Teacher_ID = t.Teacher_ID
            INNER JOIN Subjects s ON pg.Subject_ID = s.Subject_ID
            WHERE pg.Student_ID = ?
        """
        cursor.execute(query, (student_id,))
        data = cursor.fetchall()

        result = [{"Teacher_Name": row[0], "Subject": row[1], "Grade": row[2]} for row in data]

        cursor.close()
        con.close()

        return jsonify({"grades": result})

    except Exception as e:
        return jsonify({"error": str(e)})


@Authentication.route('/treferences', methods=["POST"])
def TeacherReference():
    try:
        data = request.get_json()

        sID = data["sID"]
        tID = data["tID"]
        content = data["txt"]
        date=datetime.date.today()
        sID = int(sID)
        tID =  int(tID)
        con = get_connection()
        cursor = con.cursor()


        query = """
          insert into TeacherReferencesTable values(?,?,?,?)
          """
        cursor.execute(query, (sID,tID,date,content))
        con.commit()


        cursor.close()
        con.close()

        return jsonify({"message": "Reference inserted successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})



















