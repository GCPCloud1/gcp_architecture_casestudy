from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/')  
def login():  
    return render_template("login.html")


@app.route('/validate', methods=['GET','POST'])
def validate():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        password = request.form['password']
        password = password[5:7] + "/" + password[8:] + "/" + password[:4]
        print(password)
        
        with open('patient_data.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if row[0] == first_name and row[1] == last_name and row[2] == password:
                    bp = row[3]
                    heart_rate = row[4]
                    return render_template('dashboard.html',first_name = first_name, last_name = last_name, bp=bp, heart_rate=heart_rate)
        
            error = "Invalid patient name or date of birth. Please try again."
            return render_template('login.html')
                    
    

  

if __name__ == '__main__':
    app.run(debug=True)
