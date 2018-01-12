import urllib.request
import datetime as dt
import requests


class Coin_Market_API():
	'''
	A python wrapper around coinmaketcap.com's version 1 api
	
	coinmaketcap developer notes:
		Please limit requests to no more than 10 per minute.
		Endpoints update every 5 minutes.
		API last updated November 07, 2017
	'''
	def __init__(self):
		self.api ='https://api.coinmarketcap.com/v1/'
		self.endpoint1 = 'ticker/'
		self.endpoint2 = 'global/'
		self.currency_list = ['AUD', 'BRL', 'CAD', 'CHF', 'CLP', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 
							'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK',
							'NZD', 'PHP', 'PKR', 'PLN', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'TWD', 'ZAR']
		self.coin_fields = ['id', 'name', 'symbol', 'rank', 'price_usd', 'price_btc', '24h_volume_usd',
							'market_cap_usd', 'available_supply', 'total_supply', 'max_supply',
							'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'last_updated',]
		self.market_fields = ['total_market_cap_usd', 'total_24h_volume_usd', 'bitcoin_percentage_of_market_cap',
							'active_currencies', 'active_assets', 'active_markets', 'last_updated']

	def get_coin_id(self,start=0, limit=100):
		''' 
		returns a list of coin id's.
		start 	-	return results from rank [start] and above. Should be an (int).
		limit	-	return a maximum of [limit] results. use 0 to return all results. Should be an (int).
		'''
		url = self.api + self.endpoint1 + '?' + urllib.parse.urlencode({'start': start, 'limit':limit})
		response = requests.get(url).json()
		ids = [coin['id'] for coin in response]
		return ids

	def get_single_coin_data(self,coin_id, convert=None, **kwargs):
		'''
		ticker 	- 	The id for the specific coin 
		convert - 	Return price, 24h volume, and market cap in terms of another currency. 
					Should be a (str). Valid values can be found in self.currency_list
		Example: https://api.coinmarketcap.com/v1/ticker/coin_id/
		Example: https://api.coinmarketcap.com/v1/ticker/coin_id/?convert=EUR
		**kwargs
		timestamp_format - 	The user can pass a valid datetime format string code to format the unix timestamp output.
		unix_timestamp	 -	If unix_timestamp = False the unix timestamp will be converted into the  
							default datetime string.
		include_only	 - 	A list of response feilds the user can choose to incluse. All other values will be removed. 
							Possible values can be found in self.coin_fields.
		excluded_fields	 -	A list of response feilds the user can choose to exclude.
							Possible values can be found in self.coin_fields.
		'''
		endpoint = '{}/{}/?'.format(self.endpoint1, coin_id)
		if ((convert != None) and (convert in self.currency_list)):
			url = self.api + endpoint + urllib.parse.urlencode({'convert':convert})
		else:
			url = self.api + endpoint
		response = convert_response(requests.get(url).json())
		if kwargs:
			response = self.custom_response(response, kwargs)
		return response
	
	def get_bulck_coin_data(self,*coin_id, start=0, limit=100, convert=None, **kwargs):
		'''
		*coin_id-	specific coin-id's. Please ensure that the id is within the limit of the response
		start 	-	return results from rank [start] and above. Should be an (int).
		limit	-	return a maximum of [limit] results. use 0 to return all results. Should be an (int).
		convert - 	Return price, 24h volume, and market cap in terms of another currency. 
					Should be a (str). Valid values can be found in self.currency_list
		Example: https://api.coinmarketcap.com/v1/ticker/
		Example: https://api.coinmarketcap.com/v1/ticker/?limit=10
		Example: https://api.coinmarketcap.com/v1/ticker/?start=100&limit=10
		Example: https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10
		
		**kwargs
		timestamp_format - 	The user can pass a valid datetime format string code to format the unix timestamp output.
		unix_timestamp	 -	If unix_timestamp = False the unix timestamp will be converted into the  
							default datetime string.
		include_only	 - 	A list of response feilds the user can choose to incluse. All other values will be removed. 
							Possible values can be found in self.coin_fields.
		excluded_fields	 -	A list of response feilds the user can choose to exclude.
							Possible values can be found in self.coin_fields.
		'''
		if ((convert != None) and (convert in self.currency_list)):
			url =self.api + self.endpoint1 + '?' + urllib.parse.urlencode({'start': start, 'limit':limit, 'convert':convert})
		else:
			url =self.api + self.endpoint1 + '?' + urllib.parse.urlencode({'start': start, 'limit':limit})
		response = convert_response(requests.get(url).json())
		#filter response by specific coin
		if coin_id:
			response = [coin for coin in response if coin['id'] in coin_id]
		#filter response by kwargs
		if kwargs:
			response = self.custom_response(response, kwargs)
		return response
			
	def total_coin_market_data(self, convert=None, **kwargs):		
		'''
		convert - 	Return price, 24h volume, and market cap in terms of another currency. 
					Should be a (str). Valid values can be found in self.currency_list 
		Example: https://api.coinmarketcap.com/v1/global/
		Example: https://api.coinmarketcap.com/v1/global/?convert=EUR
		**kwargs
		timestamp_format - 	The user can pass a valid datetime format string code to format the unix timestamp output.
		unix_timestamp	 -	If unix_timestamp = False the unix timestamp will be converted into the  
							default datetime string.
		include_only	 - 	A list of response feilds the user can choose to incluse. All other values will be removed. 
							Possible values can be found in self.coin_fields.
		excluded_fields	 -	A list of response feilds the user can choose to exclude.
							Possible values can be found in self.coin_fields.
		'''
		if ((convert != None) and (convert in self.currency_list)):
			url = self.api + self.endpoint2 + '?' + urllib.parse.urlencode({'convert':convert})
		else:
			url = self.api + self.endpoint2
		response = convert_response(requests.get(url).json())
		if kwargs:
			response = self.custom_response(response, kwargs)
		return response

	def custom_response(self, response, kwargs):
		'''Manipulates a response by the parent functions **kwargs'''
		#check for custom timestamp formating
		if 'timestamp_format' in kwargs.keys():
			response = self.response_timestamp_to_date(response, kwargs['timestamp_format'])
		#check for default timestamp formating:
		elif  'unix_timestamp' in kwargs.keys():
			#check if unix_timestamp is false
			if not kwargs['unix_timestamp']:
				response = self.response_timestamp_to_date(response)
		#only include certain feilds
		if 'include_only' in kwargs.keys() and (type(kwargs['include_only']) == list):
			response = self.only_fields(response, kwargs['include_only'])
		#exclude certain feilds
		if ('excluded_fields' in kwargs.keys()) and (type(kwargs['excluded_fields']) == list):
			response = self.exclud_fields(response, kwargs['excluded_fields'])

		return response

	def response_timestamp_to_date(self, response, timestamp_format='%m/%d/%Y %I:%M:%S %p'):
		'''
		Converts the 'last_updated' field for each coin in the response to the given timestamp_format
		'''
		if response != []:
			for coin in response:
				coin['last_updated'] = dt.datetime.strftime(dt.datetime.fromtimestamp(int(coin['last_updated'])), timestamp_format)
		
		return response

	def exclud_fields(self, response, feild_list):
		if feild_list != [] and response != []:
			for coin in response:
				for field in feild_list:
					try:
						coin.pop(field)
					except KeyError:
						pass
		return response

	def only_fields(self, response, feild_list):
		if feild_list != [] and response != []:
			new_reponse = []
			for coin in response:
				update_coin = {}
				for key in coin.keys():
					if key in feild_list:
						update_coin[key] = coin[key]
				if update_coin != {}:
					new_reponse.append(update_coin)
			response = new_reponse
		return response

def convert_response(response):
	'''
	Originally the response only returns string values.
	This function will attempt to convert number values into Floats
	'''
	if response != []:
		for coin in response:
			for key in coin.keys():	
				try:
					coin[key] = float(coin[key])	
				except ValueError:
					pass
				except TypeError:
					pass
	return response
					
				
				




