from yahoo_finance import Share
print "Yahoo! Package imported."
filelist = open('list_of_companies.txt', 'r')
print "File opened."
names=[];
companies=[];
jsonlist=[];

for line in filelist:
	names.append(line.rstrip('\n\r').split(',')[0])
	companies.append(line.rstrip('\n\r').split(',')[1])
	print line.rstrip('\n\r'), "added."
	print "Requesting JSON for", line.rstrip('\n\r')
	jsonlist.append(Share(line.rstrip('\n\r').split(',')[1]))
	print "JSON added for", line.rstrip('\n\r')
	print

filelist.close();

from models import Company
from database import db_session
for i in range(len(companies)):
	print ""
	company = jsonlist[i];
	try:
		price = float(company.get_price())
		dividend_share = float(company.get_dividend_share())
		earnings_share = float(company.get_earnings_share())
		dividend_payout_ratio = dividend_share/earnings_share

		print companies[i]
		print "Price:", price
		print "Divident Per Share:", dividend_share
		print "Earnings Per Share:", earnings_share
		print "Dividend Payout Ratio:", dividend_payout_ratio
		q = Company.query.filter_by(symbol=companies[i]).first()
		if q is None:
			q = Company(names[i], companies[i], price, dividend_share, earnings_share, dividend_payout_ratio)
			db_session.add(q)
			db_session.commit()
			print "Added ", companies[i]
		else:
			q.price=price
			q.dps=dividend_share
			q.eps=earnings_share
			q.dpr=dividend_payout_ratio
			db_session.commit()
			print "Updated ", companies[i]
	except:
		print "Error with ", companies[i]
		continue