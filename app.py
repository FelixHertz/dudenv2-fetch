from flask import Flask, render_template, request, flash
import time
from datetime import datetime
import base64
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import mysql.connector

mydb = mysql.connector.connect(host="sql11.freesqldatabase.com", user="sql11524700", passwd="tY17NVeXtN", database="sql11524700")
mycursor = mydb.cursor()

def retrieve():
	sql = "SELECT wort FROM wort_erg"
	mycursor.execute(sql)
	




## Create Flask App
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"


## Routing of Sub - Pages


@app.route("/")
def index():
    return render_template("index.html") 
   



@app.route("/liste", methods=['POST', 'GET'])
def greeter():
	retrieve()
	for i in mycursor:
		flash(i)
	return render_template("index.html")

