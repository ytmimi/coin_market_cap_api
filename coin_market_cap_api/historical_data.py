import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import pandas as pd
import datetime as dt


def start_and_end(offset):
	'''
	offset: Should be a datetime.timedelta object specifying 
	returns the start and end dates as strings formated in YYYYMMDD form.
	'''
	dt_format = '%Y%m%d'
	today = dt.date.today()
	begging = today - offset
	end = dt.date.strftime(today, dt_format)
	start = dt.date.strftime(begging, dt_format)
	return [start, end]



class Historical_Data():
	'''
	A web scraper that gets some historical data from the coinmarketcap.com website.
	The data only includes daily Open, High, Low, Close, Volume, and Market-Cap figures.
	Data for some coins may be incomplete.
	'''
	def __init__(self, coin_id):
		self.coin_id = coin_id
		self.url = 'https://coinmarketcap.com/currencies/{}/historical-data/'.format(self.coin_id)

		
	def generate_table(self, url=''):
		if url != '':
			request = requests.get(url).text
		else:
			request = requests.get(self.url).text
		#Beautiful soup object
		soup = BeautifulSoup(request, 'html.parser')
		#Empty OrderdDict
		table_data = OrderedDict()
		#first element found in find_all
		table = soup.find_all('table', class_= 'table')[0]
		#all elements in the tables header
		table_header = table.thead
		#all elements in the tables body
		table_body = table.tbody

		#Creates keys in the table_data dict using the table headers
		for header in table_header.find_all('th'):
			table_data[header.text] = []
		#Creats a list out of the newly added dict keys
		table_keys = list(table_data.keys())
		#Adds the data from each row to the appropriate list in table_data
		for row in table_body.find_all('tr'):
			for i, data in enumerate(row.find_all('td')):
				try:
					date = dt.datetime.strptime(data.text, '%b %d, %Y')
					table_data[table_keys[i]].append(date)
				except:
					table_data[table_keys[i]].append(data.text)
		
		df = pd.DataFrame(table_data)
		df.set_index(table_keys[0], inplace=True)
		return df

	def last_7_days(self):
		dates = start_and_end(dt.timedelta(days=7))
		url = self.url +'?start={}&end={}'.format(dates[0], dates[1])
		return self.generate_table(url)

	def last_30_days(self):
		dates = start_and_end(dt.timedelta(days=30))
		url = self.url +'?start={}&end={}'.format(dates[0], dates[1])
		return self.generate_table(url)

	def last_3_months(self):
		#a month is estimated to have 30 days
		dates = start_and_end(dt.timedelta(days=90))
		return self.generate_table(url)

	def last_12_months(self):
		#a month is estimated to have 30 days
		dates = start_and_end(dt.timedelta(days=360))
		return self.generate_table(url)



if __name__ == '__main__':
	h = Historical_Data('ethereum').last_30_days()
	print(h)



		

 


	

	

	