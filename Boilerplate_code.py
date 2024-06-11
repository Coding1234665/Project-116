#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/Boilerplate_code")
def student_webpage():
    name = 'Manvith'
    return render_template('activity.html', student_name = name)
app.run(debug=True)

#‘/’ URL is bound with first_flask function.


    

#run the application on local server

