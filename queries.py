# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()

from models import Company
from database import db_session

from sqlalchemy import desc

def ratiowise(ratio_name, lower_limit, upper_limit):
	ratios=["price", "dps", "eps", "dpr"]
	try:
		if ratio_name not in ratios:
			return "Invalid Ratio"
		else:
			q=db_session.query(Company).order_by(getattr(Company, ratio_name).desc()).all()
			if(lower_limit==0.0 and upper_limit==0.0):
				return q[0].name
				# return q[:5]
				#query top 5 ratios
			else:
				if(upper_limit==0.0):
					#query by lowerlimit
					return_list=[]
					for i in q:
						if getattr(i, ratio_name) >= lower_limit :
							return_list.append(i)
					if len(return_list) == 0 :
						return "No records"
					else:
						return return_list[0].name
						# return return_list
				else:
					#query between upper and lower
					return_list=[]
					for i in q:
						if getattr(i, ratio_name) >= lower_limit and getattr(i, ratio_name) <= upper_limit :
							return_list.append(i)
					if len(return_list) == 0 :
						return "No records"
					else:
						return return_list[0].name
						# return return_list
	except:
		return "Error"

def companywise(company_symbol):
	try:
		company_query=Company.query.filter_by(symbol=company_symbol).first()
		return company_query.name
	except:
		return "Company Not Found"


