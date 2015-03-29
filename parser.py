import re, urllib2   
url = raw_input()
xml=urllib2.urlopen(url)
f=xml.read()
print re.search(r'(Current Ratio.*\n.*\n.*<td.*">)(.*)(</td>)',f).group(2)
print re.search(r'(Quick Ratio.*\n.*\n.*<td.*">)(.*)(</td>)',f).group(2)
print re.search(r'(Debt Equity Ratio.*\n.*\n.*<td.*">)(.*)(</td>)',f).group(2)
print re.search(r'(Long Term Debt Equity Ratio.*\n.*\n.*<td.*">)(.*)(</td>)',f).group(2)