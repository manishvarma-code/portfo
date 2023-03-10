from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')
	
	

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)	



def write_csv(data):
	with open('database.csv', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		messege = data["messege"]
		csv_writer = csv.writer(database2, delimiter=',',  quotechar='|', quoting=csv.QUOTE_MINIMAL) 
		csv_writer.writerow([email,subject,messege])    



def write_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		messege = data["messege"]
		file = database.write(f'\n{email}, {subject}, {messege}')  






@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
     
     if request.method == 'POST':
     	data = request.form.to_dict()
     	write_csv(data)
     	return redirect('/thankyou.html')
     else:
     	return 'somthing went wrong please try again later!'
     


     
