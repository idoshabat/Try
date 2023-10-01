from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('web.html')


# @app.route('/<string:page_name>')
# def hello(page_name):
#     return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        add_date_csv(data)
        return 'form submitted successfully!!!'
    else:
        print("Something went wrong!")


def add_date(data):
    if not isinstance(data, dict):
        print("Error")
        return

    try:
        with open('database.txt', mode='a') as my_data:
            my_data.write('\n'+data.__str__())
            print("Success!!")
    except FileNotFoundError:
        print("something went wrong, not such file")


def add_date_csv(data):
    if not isinstance(data, dict):
        print("Error")
        return

    first_name=data['firstName']
    last_name=data['lastName']
    amount=data['amount']
    date=data['date']
    transaction_Type=data['transaction_type']

    try:
        with open('database2.csv',newline='', mode='a') as my_data2:
            csv_wrtier=csv.writer(my_data2, delimiter=',' ,quotechar='"',quoting=csv.QUOTE_MINIMAL)
            csv_wrtier.writerow([first_name,last_name,amount,date,transaction_Type])
            print("Success!!")
    except FileNotFoundError:
        print("something went wrong, not such file")