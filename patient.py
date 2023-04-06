from flask import Flask,render_template,request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/patient-login')
def patient():
    return render_template('patient-login.html')

@app.route('/validate', methods =['GET','POST'])
def validate():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        password = request.form['password']
        print(password)
        password = password[5:7] + "/" + password[8:] + "/" + password[:4]
        print(password)
        
        with open('patient_data.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if row[1] == first_name and row[2] == last_name and row[3] == password:
                    bp = row[12]
                    heart_rate = row[11]
                    return render_template('patient-db.html',first_name = first_name, last_name = last_name, bp=bp, heart_rate=heart_rate)
        
            error = "Invalid patient name or date of birth. Please try again."
            return render_template('patient-login.html',error=error)

                        

if __name__ == '__main__':
    app.run(debug=True)
