# from database import db_session

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()

from models import Company
from database import db_session

def ratiowise(ratio_name, lower_limit, upper_limit):
	ratios=["price", "dps", "eps", "dpr"]
	try:
		if ratio_name not in ratios:
			return "Invalid Ratio"
		else:
			if(lower_limit==0.0 and upper_limit==0.0):
				#query top 5 ratios
			else:
				if(upper_limit==0.0):
					#query by lowerlimit
				else:
					#query between upper and lower
	except:
		return "Error"

def companywise(company_symbol):
	try:
		company_query=Company.query.filter_by(symbol=company_symbol).first()
		return company_query.name
	except:
		return "Error"


