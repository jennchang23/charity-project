from flask import Flask, render_template
import datetime
import json
​
# Import our pymongo library, which lets us connect to our mongo DB
import pymongo
​
# Create an instance of our Flask app 
app = Flask(__name__)
​
# Create connection variable
conn = 'mongodb+srv://falcon2020:Falcon20@charity-cluster-homax.azure.mongodb.net/test?retryWrites=true&w=majority'
​
# Pass connection to the pymongo instance
client = pymongo.MongoClient(conn)
​
# Connect to the database
db = client.charity_orgs
​
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
​
# Set routes
## Route for Homepage
@app.route('/')
def index():
    # # Store the entire charity collection in a list 
    # index = list(db.main_info.find({}))
​
    # Return the template with the charities list passed in 
    return render_template('index.html')
​
## Route for Charity Details Page
@app.route('/charity-details.html')
def charity_details():
    # Store the entire charity collection in a list 
    # charity_details = list(db.main_info.find({},{"mission":1, "websiteURL":1,"charityName":1,"cause":1, "mailingAddress":1}))
    charity_details = list(db.main_clean.find({}))
​
    # Return the template with the charities list passed in 
    return render_template('charity-details.html', charity_details=json.dumps(charity_details, default = myconverter))
​
## Route for Expense Details Page
@app.route('/expense-details.html')
def expense_details():
    # Store the organizations' financial info in a list
    expense_details = list(db.org_clean.find({}))
​
    # Return the template with the charities list passed in 
    return render_template('expense-details.html', expense_details=json.dumps(expense_details, default = myconverter))
​
## Route for US Charity Info Page
@app.route('/us-charity-info.html')
def us_info():
    # Store the entire charity collection in a list 
    us_info = list(db.main_clean.find({}))
​
    # Return the template with the charities list passed in 
    return render_template('us-charity-info.html', us_info=json.dumps(us_info, default = myconverter))
    
if __name__=="__main__":
    app.run(debug=True)