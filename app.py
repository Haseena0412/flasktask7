from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template('/index.html')

@app.route('/welcome',methods=['POST'])
def welcome():
    name=request.form['name']
    age = int(request.form['age'])
    if age >= 18:
        return f"Hello {name} You can vote!"
    else:
        return f"Hello {name} You cannot vote."
if __name__=="__main__":
    app.run(debug=True)