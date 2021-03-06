# from dbhelper import DBHelper
# from mockdbhelper import MockDBHelper as DBHelper  # For local testing purposes

from flask import Flask
from flask import render_template
from flask import request
import dbconfig

if dbconfig.test:
    from mockdbhelper import MockDBHelper as DBHelper
    print("Using mockdbhelper, test: " +
          str(dbconfig.test))  # For testing purposes
    print(dbconfig.gmapsapi)
else:
    from dbhelper import DBHelper
    print("Using dbhelper, test: " + str(dbconfig.test))  # For testing purposes

app = Flask(__name__)
DB = DBHelper()


@app.route("/")
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as e:
        print(e)
        data = None
    return render_template("home.html", data=data)


@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.form.get("userinput")
        DB.add_input(data)
    except Exception as e:
        print(e)
    return home()


@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print(e)
    return home()


@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    category = request.form.get("category")
    date = request.form.get("date")
    latitude = float(request.form.get("latitude"))
    longitude = float(request.form.get("longitude"))
    description = request.form.get("descriptioon")
    DB.add_crime(category, date, latitude, longitude, description)
    return home()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
