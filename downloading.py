from urllib import request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1529745544&period2=1532337544&interval=1d&events=history&crumb=6hrLU.NinRP'

def download_stock_data(csv_url):
	response = request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n") #Breaks in new line
	dest_url = r'goog.csv'
	fx = open(dest_url,"w")
	for line in lines:
		fx.write(line +"\n")
	fx.close()

download_stock_data(goog_url)
