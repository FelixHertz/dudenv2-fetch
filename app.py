from flask import Flask, render_template, request, flash
import mysql.connector

mydb = mysql.connector.connect(host="h1.host.filess.io", user="dudenv2_bystreamwe", passwd="239848e4ad651c7b21981c6cd1fea4bf6ec5c444", database="dudenv2_bystreamwe", port="3307")
mycursor = mydb.cursor()


def retrieve():
	sql = "SELECT wort FROM wort_erg"
	mycursor.execute(sql)



def retrieve_gebrauch_other():
	sql = "SELECT gebrauch FROM other"
	mycursor.execute(sql)

## Create Flask App
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
retrieve_gebrauch_other()
gebrauch_other = []
for i in mycursor:
	if not gebrauch_other:
		gebrauch_other.append(i)



## Routing of Sub - Pages


@app.route("/")
def index():
	retrieve()
	latest = "Resuemieren"
	for i in mycursor:
		latest = i
	flash(''.join(latest), 'category1')
	return render_template("index.html")
   

@app.route("/liste", methods=['POST', 'GET'])
def greeter():
	cur = mydb.cursor()
	cur.execute("SELECT * FROM wort_erg")
	data = cur.fetchall()

	return render_template("liste.html", data=data, alle=False, list=True)


@app.route("/alles", methods=['POST', 'GET'])
def all():
	cur = mydb.cursor()
	cur.execute("SELECT * FROM other")
	data = cur.fetchall()
	return render_template("liste.html", data=data, alle=True, list=False)



for i in gebrauch_other:
	@app.route("/<i>", methods=['POST', 'GET'])
	def variable(i):
		cur = mydb.cursor()
		cur.execute("SELECT * FROM other WHERE gebrauch='%s'" % i)
		data = cur.fetchall()
		return render_template("liste.html", data=data, alle=False, list=False, custom=True, gebrauch=i)
		

	