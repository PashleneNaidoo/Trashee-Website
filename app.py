from flask import Flask,render_template, jsonify


JOBS=[{
  'title':'Paper',
  'Conditon': 'One or more bin bags',
  'Reward' : '2 tokens'
},
{
  'title':'Plastic',
  'Conditon': 'One or more bin bags',
  'Reward' : '2 tokens'
},
{
  'title':'Aluminium',
  'Conditon': 'One or more bin bags',
  'Reward' : '2 tokens'
},
{
  'title':'Metal',
  'Conditon': 'One or more shopping bags',
  'Reward' : '2 tokens'
},
{
  'title':'Copper',
  'Conditon': 'One or more shopping bags',
  
}
]



app=Flask(__name__)

@app.route('/')
def hello_Trashee():
  return render_template('home.html',jobs=JOBS,company_name="Trashee")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)