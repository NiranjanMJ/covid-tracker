from flask import Flask , request

app = Flask(__name__)
import mysql.connector



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name')
def hello_name():
    return 'Hello, Niranjan!'


@app.route('/covid/', methods=['GET'])
def get_covid():
    # state_name = request.args.get('state' , None)
    #
    # mydb = mysql.connector.connect(
    #     host="localhost" ,
    #     user="root" ,
    #     password="Global!23",
    #     database="covidtrackerdb"
    # )
    # mycursor = mydb.cursor()
    # mycursor.execute("SELECT * FROM Tracker where statename='kerala'" )
    #
    # myresult = mycursor.fetchall()
    return "{ affected_count : 0,recovered_count: 0}"

@app.route('/covid/add/', methods=['POST'])
def post_covid():
    # state_name = request.args.get('state' , None)
    #
    # mydb = mysql.connector.connect(
    #     host="localhost" ,
    #     user="root" ,
    #     password="Global!23",
    #     database="covidtrackerdb"
    # )
    # mycursor = mydb.cursor()
    # mycursor.execute("Update Tracker set affected = 50" )
    #
    # myresult = mycursor.fetchall()
    return True

if __name__ == '__main__':
    app.run(port=5001)