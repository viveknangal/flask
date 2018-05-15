from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route("/")
def index():
    #return "Hello, World!"
    return render_template("input.html")

@app.route("/input", methods=['POST'])
def getdata():
#	query = request.args.get("fname")
	query = request.form.get("fname")
	name_list=['vivek','gauri']
    	return render_template("home.html",heading=query,name_list=name_list,counter=1)
if __name__ == '__main__':
	app.run()
