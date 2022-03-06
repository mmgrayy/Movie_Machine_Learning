from flask import Flask, render_template
from flask import *
from functools import wraps
import sqlite3

app = Flask(__name__)
@app.route('/')
def home():
   return render_template('web_page/index.html')

@app.route('/generate')
def generate():
   print ('Hello World!')
   return render_template('index.html')

