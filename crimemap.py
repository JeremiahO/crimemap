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


if __name__ == '__main__':
    app.run(port=5000, debug=True)
