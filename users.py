import pyodbc
from flask import request, jsonify, Blueprint
import  datetime

def get_connection():

    try:
        conn = pyodbc.connect(

            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=LIVW1012\\SQLEXPRESS;"
            "DATABASE=Education_DB;"
            "Trusted_Connection=yes;"

        )

        return conn

    except Exception as e:
        print (f"Database Connection Failed {e}")

# API for Users

Register_user = Blueprint('User', __name__)
@Register_user.route('/Registration', methods= ['POST'])
def SumNumber():
    try:
        data = request.get_json()

        name=data["name"]
        email = data["email"]
        password = data["password"]
        dob = data["dob"]
        role = data["role"]

        current_date = datetime.date.today()


        con  =get_connection()
        cursor = con.cursor()
        cursor.execute(
             "insert into Users ( Name, Email_Address , Password,DateOfBirth,Date_Created,Role) Values (?,?,?,?,?,?)",
            (name,email,password,dob,current_date,role)
        )
        con.commit()
        cursor.close()
        con.close()

        return jsonify({"message" : "use inserted successfully"})

    except Exception as e :
        return jsonify({"message":f"error inserting user {e}"})


