from flask import Flask
from queries import companywise
from queries import ratiowise
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World! :D'

@app.route('/company/<company_symbol>')
def show_company(company_symbol):
	return companywise(company_symbol)

@app.route('/ratio/<ratio_name>/<float:lower_limit>/<float:upper_limit>')
def show_ratio(ratio_name, lower_limit, upper_limit):
	return ratiowise(ratio_name, lower_limit, upper_limit)

if __name__ == '__main__':
	app.debug = True
	app.run() # to run on local machine
	 # app.run(host='0.0.0.0') # to make accessbile to public IPs