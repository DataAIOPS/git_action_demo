'''
URL Format 
http://localhost:5000/apidocs
'''

from flask import Flask,request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/substraction')
def substraction():
    """Click here
    ---
    parameters:
        - name: a
          in: query
          type: number
          required: true
        - name: b
          in: query
          type: number
          required: true
    responses:
          200:
              description: Here is substraction
    """
    a=request.args.get("a")
    b=request.args.get("b")
    c=int(b)-int(a)
    return f"substraction of {b}-{a}={c}"

@app.route('/addition')
def addition():
    """Click here
    ---
    parameters:
        - name: a
          in: query
          type: number
          required: true
        - name: b
          in: query
          type: number
          required: true
    responses:
          200:
              description: Here is substraction
    """
    a=request.args.get("a")
    b=request.args.get("b")
    c=int(b)+int(a)
    return f"addition of {b}+{a}={c}"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)