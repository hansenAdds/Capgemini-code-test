from flask import Flask, request ,render_template, jsonify
from flask_restful import Resource, Api 
import numpy as np
import math 
from functools import reduce
from regex import P
from sqlalchemy import false

app = Flask(__name__)
api = Api(app)



@app.route('/hello')
def hello_world():
   return {'hello':'hello world'}
   
@app.route('/resume')
def hello_name():
   return render_template('resume.html')

@app.route('/', methods=["POST","GET"])
def default_page():
   getData = request.args.to_dict()
   list_data=list(getData.values())
   tempdata=list(map(float, list_data[0][1:-1].split(",")))
   data=reduce_function(tempdata)

   return render_template('index.html',content=getData,result=data)
   


def reduce_function(data):
 
   data.sort()
   c= data[-3:]
   squared = reduce(lambda x,y: math.sqrt(x**2+y**2), c)
   return round(squared,2)
   

if __name__ == '__main__':
    app.run(debug=True)