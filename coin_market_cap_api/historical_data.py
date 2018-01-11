import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import pandas as pd
import datetime as dt

class Historical_Data():
	'''
	A web scraper that gets some historical data from the coinmarketcap.com website.
	The data only includes daily Open, High, Low, Close, Volume, and Market-Cap figures.
	Data for some coins may be incomplete.
	'''
	def __init__(self, coin_id):
		self.url = 'https://coinmarketcap.com/currencies/{}/historical-data/'.format(coin_id)
		self.request = requests.get(self.url).text
		self.data_table = self.generate_table()

	def __str__(self, rows=5):
		return '{}'.format(self.data_table.head(rows))
		
	def generate_table(self):
		#Beautiful soup object
		soup = BeautifulSoup(self.request, 'html.parser')
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




		

 


	

	

	